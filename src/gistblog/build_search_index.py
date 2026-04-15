import os
import json
import re
from datetime import datetime

CONTENT_DIR = "content"
STATIC_DIR = "static"

RST_BORDER = re.compile(r'^[=\-~^"\'`#+*]{2,}$')


def simple_slugify(text):
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[\s-]+', '-', text)


def is_border(line):
    """True if the line is a pure RST section-title border (===, ---, etc.)."""
    return bool(RST_BORDER.match(line.strip())) and len(line.strip()) >= 2


def parse_rst_file(filepath):
    """
    Return (title, metadata_dict, body_lines) from an RST file.

    Handles both title styles:
      Style A - overline + title + underline  (lines 0-1-2)
      Style B - title + underline             (lines 0-1)

    After the title block, a contiguous run of :key: value lines is
    consumed as metadata; everything after that is the body.
    """
    with open(filepath, encoding='utf-8') as fh:
        lines = fh.read().splitlines()

    # Strip leading blank lines
    while lines and not lines[0].strip():
        lines.pop(0)

    title = None
    i = 0

    if len(lines) >= 3 and is_border(lines[0]) and is_border(lines[2]):
        # Style A: overline / title / underline
        title = lines[1].strip()
        i = 3
    elif len(lines) >= 2 and not is_border(lines[0]) and is_border(lines[1]):
        # Style B: title / underline
        title = lines[0].strip()
        i = 2
    else:
        # Fallback: first non-empty line is the title
        title = lines[0].strip() if lines else 'Untitled'
        i = 1

    # Skip any blank lines between title block and metadata
    while i < len(lines) and not lines[i].strip():
        i += 1

    # Consume metadata block (:key: value)
    metadata = {}
    while i < len(lines):
        m = re.match(r'^:(\w[\w-]*):\s*(.*)', lines[i].strip())
        if m:
            metadata[m.group(1)] = m.group(2).strip()
            i += 1
        else:
            break

    body_lines = lines[i:]
    return title or 'Untitled', metadata, body_lines


def clean_rst_body(lines):
    """Return plain text from RST body lines, stripping markup and directives."""
    out = []
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        if is_border(s):
            continue
        if s.startswith('.. '):        # RST directive
            continue
        # Remove inline markup
        s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)   # **bold**
        s = re.sub(r'\*(.+?)\*',     r'\1', s)   # *italic*
        s = re.sub(r'``(.+?)``',     r'\1', s)   # ``code``
        s = re.sub(r':\w+:`(.+?)`',  r'\1', s)   # :role:`text`
        s = re.sub(r'`(.+?)`_?',     r'\1', s)   # `ref`_
        s = re.sub(r'^\s*[-*+]\s+',  '',    s)   # bullet markers
        if s:
            out.append(s)
    return ' '.join(out)


def build_search_index():
    """Generate a JSON index of all posts for the search feature."""
    if not os.path.exists(STATIC_DIR):
        os.makedirs(STATIC_DIR)

    posts = []
    for filename in sorted(os.listdir(CONTENT_DIR)):
        if not filename.endswith('.rst') or filename.startswith('.'):
            continue

        filepath = os.path.join(CONTENT_DIR, filename)
        title, metadata, body_lines = parse_rst_file(filepath)

        date_str = metadata.get('date', '')
        try:
            date = datetime.fromisoformat(date_str.replace(' ', 'T')) if date_str else datetime.now()
        except Exception:
            date = datetime.now()

        category = metadata.get('category', 'Uncategorized')
        tags_raw = metadata.get('tags', '')
        tags = [t.strip() for t in tags_raw.split(',')] if tags_raw else []
        summary = metadata.get('summary', '').strip()

        slug = simple_slugify(title)
        url = f"posts/{date.strftime('%Y/%m')}/{slug}/"

        body_text = clean_rst_body(body_lines)
        if len(body_text) > 1000:
            body_text = body_text[:1000] + '...'

        posts.append({
            'title': title,
            'url': url,
            'date': date.strftime('%Y-%m-%d'),
            'category': category,
            'tags': tags,
            'summary': summary,
            'content': body_text,
        })

    with open(os.path.join(STATIC_DIR, 'search_index.json'), 'w', encoding='utf-8') as fh:
        json.dump(posts, fh, ensure_ascii=False, indent=2)

    print(f"Generated search index with {len(posts)} posts")


if __name__ == '__main__':
    build_search_index()
