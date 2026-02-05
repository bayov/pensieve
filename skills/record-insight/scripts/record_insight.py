#!/usr/bin/env python3
import argparse
import datetime
import os
import re
import sys


def sanitize_slug(slug):
    """Sanitizes the slug to snake_case."""
    # Replace non-alphanumeric characters (except underscores) with underscores
    slug = re.sub(r'[^a-zA-Z0-9_]', '_', slug)
    # Convert to lowercase
    slug = slug.lower()
    # Remove consecutive underscores
    slug = re.sub(r'_+', '_', slug)
    # Strip leading/trailing underscores
    slug = slug.strip('_')
    return slug


def main():
    parser = argparse.ArgumentParser(
        description="Record a permanent insight into the Pensieve.")
    parser.add_argument("--slug", required=True,
                        help="A short topic string (e.g., 'docker_permission_fix').")
    parser.add_argument("--path", required=True,
                        help="The directory path this insight applies to.")
    parser.add_argument("--trigger", required=True,
                        help="The context or error that caused the insight.")
    parser.add_argument("--insight", required=True,
                        help="The detailed lesson, fix, constraint, etc.")
    args = parser.parse_args()

    # Validate that the provided path exists
    if not os.path.exists(args.path):
        print(f"Error: The provided --path \"{args.path}\" does not exist.",
              file=sys.stderr)
        sys.exit(1)

    # Configuration
    insights_dir = ".pensieve/insights"

    # Ensure the insights directory exists
    if not os.path.exists(insights_dir):
        try:
            os.makedirs(insights_dir)
        except OSError as e:
            print(f"Error: Could not create directory '{insights_dir}': {e}",
                  file=sys.stderr)
            sys.exit(1)

    # Sanitize slug
    safe_slug = sanitize_slug(args.slug)
    if not safe_slug:
        print("Error: Invalid slug provided.", file=sys.stderr)
        sys.exit(1)

    # Generate timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d.%H-%M-%S")

    # Construct filename
    filename = f"{timestamp}.{safe_slug}.md"
    file_path = os.path.join(insights_dir, filename)

    # Content format
    content = f"""---
path: {args.path}
---

# Insight
{args.insight}

# Trigger
{args.trigger}
"""

    # Write the insight file
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Insight recorded successfully: {file_path}")
    except IOError as e:
        print(f"Error: Could not write to file '{file_path}': {e}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
