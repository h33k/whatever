import os
import re
from datetime import datetime
import yaml

def get_current_mds():
    posts_dir = "../docs/_posts"
    if not os.path.isdir(posts_dir):
        return []

    md_files = [
        filename for filename in os.listdir(posts_dir)
        if filename.endswith(".md") or filename.endswith(".markdown")
    ]
    return md_files


def get_md(full_filename, posts_dir="_posts"):
    if not os.path.isdir(posts_dir):
        return None

    full_path = os.path.join(posts_dir, full_filename)
    if os.path.isfile(full_path):
        return full_path

    return None


def is_modified(date_prefix, modified_when, posts_dir="../docs/_posts"):
    import os, re, yaml
    from datetime import datetime

    for filename in os.listdir(posts_dir):
        if filename.startswith(date_prefix) and filename.endswith((".md", ".markdown")):
            filepath = os.path.join(posts_dir, filename)
            break
    else:
        return True

    try:
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return True

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return True

    frontmatter = yaml.safe_load(match.group(1))
    if 'modified_when' not in frontmatter:
        return True

    val = frontmatter['modified_when']
    if isinstance(val, datetime):
        val = val.strftime('%Y-%m-%d %H:%M:%S.%f')
    else:
        val = str(val)

    mod = modified_when.replace('T', ' ')

    def norm(s):
        if '.' not in s:
            return s
        d, micro = s.split('.', 1)
        micro = (micro + '000000')[:6]
        return f"{d}.{micro}"

    return norm(val.strip()) != norm(mod.strip())


def delete_md_with_date_prefix(date_prefix, posts_dir="../docs/_posts"):
    for filename in os.listdir(posts_dir):
        if filename.startswith(date_prefix) and filename.endswith((".md", ".markdown")):
            filepath = os.path.join(posts_dir, filename)
            try:
                os.remove(filepath)
                print(f"File {filename} deleted.")
                return True
            except Exception as e:
                print(f"Error while deleting file {filename}: {e}")
                return False
    print("File with this prefix was not found.")
    return False