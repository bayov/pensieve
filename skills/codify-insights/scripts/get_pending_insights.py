#!/usr/bin/env python3
import os
import re
import json
import sys

INSIGHTS_DIR = ".pensieve/insights"

def parse_frontmatter(content):
    """
    Extracts YAML frontmatter from markdown content.
    Returns a dict of key-value pairs.
    """
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}
    
    yaml_block = match.group(1)
    data = {}
    for line in yaml_block.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Remove quotes
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            data[key] = value
    return data

def get_grouped_insights():
    if not os.path.exists(INSIGHTS_DIR):
        print("[]")
        return

    grouped_dict = {}

    for filename in sorted(os.listdir(INSIGHTS_DIR)):
        if not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(INSIGHTS_DIR, filename)
        if not os.path.isfile(filepath):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            meta = parse_frontmatter(content)
            
            parts = content.split('---', 2)
            body = parts[2].strip() if len(parts) > 2 else ""
            if not body and not meta:
                body = content

            target_path = meta.get("path", ".")
            
            entry = {
                "filename": filename,
                "slug": meta.get("slug", "unknown"),
                "trigger": meta.get("trigger", "No trigger provided"),
                "content": meta.get("insight", "") or body
            }

            if target_path not in grouped_dict:
                grouped_dict[target_path] = []
            grouped_dict[target_path].append(entry)

        except Exception as e:
            sys.stderr.write(f"Error parsing {filename}: {e}\n")

    # Convert dictionary to a list of groups for cleaner JSON iteration
    output = []
    for path, insights in grouped_dict.items():
        output.append({
            "target_path": path,
            "insights": insights
        })

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    get_grouped_insights()