import os
import shutil

import requests

# Configuration
USERNAME = "barseghyanartur"
GIST_API = f"https://api.github.com/users/{USERNAME}/gists"
CONTENT_DIR = "content"
PAGES_DIR = os.path.join(CONTENT_DIR, "pages")
TEMP_PAGES = "temp_pages"


def fetch_data():
    """
    Fetches all public gists for a user, filters by description prefix,
    and saves the raw content as .rst files while preserving local static pages.
    """
    pages_backup = None

    # 1. Back up existing static pages if they exist
    if os.path.exists(PAGES_DIR):
        pages_backup = TEMP_PAGES
        if os.path.exists(pages_backup):
            shutil.rmtree(pages_backup)
        shutil.copytree(PAGES_DIR, pages_backup)

    # 2. Refresh the content directory
    if os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)
    os.makedirs(CONTENT_DIR)

    # 3. Restore static pages from backup
    if pages_backup and os.path.exists(pages_backup):
        os.makedirs(PAGES_DIR, exist_ok=True)
        shutil.copytree(pages_backup, PAGES_DIR, dirs_exist_ok=True)
        shutil.rmtree(pages_backup)

    # 4. Prepare API request headers
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    # Use a session for connection pooling (faster for multiple requests)
    session = requests.Session()
    session.headers.update(headers)

    page = 1
    synced_count = 0

    print(f"Starting sync for user: {USERNAME}...")

    # 5. Pagination loop to fetch ALL gists
    while True:
        params = {
            "page": page,
            "per_page": 100  # Maximize items per request
        }

        response = session.get(GIST_API, params=params)
        response.raise_for_status()
        
        gists = response.json()
        
        # Break if no more gists are found
        if not gists:
            break

        for gist in gists:
            description = gist.get('description') or ""
            
            # Filter gists intended for the blog
            if description.startswith("blog:"):
                # Get the first file in the gist
                files = gist.get('files', {})
                if not files:
                    continue
                    
                file_meta = list(files.values())[0]
                raw_url = file_meta['raw_url']
                
                # Fetch the actual content of the gist
                content_res = session.get(raw_url)
                content_res.raise_for_status()
                content = content_res.text

                # Save to disk
                filename = f"{gist['id']}.rst"
                filepath = os.path.join(CONTENT_DIR, filename)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                
                print(f"Synced: {description} -> {filename}")
                synced_count += 1
        
        page += 1

    print(f"Finished. Total gists synced: {synced_count}")


if __name__ == "__main__":
    fetch_data()
