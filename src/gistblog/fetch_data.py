import os
import sys
import shutil

import httpx

USERNAME = "barseghyanartur"
GIST_API = f"https://api.github.com/users/{USERNAME}/gists"
CONTENT_DIR = "content"
PAGES_DIR = os.path.join(CONTENT_DIR, "pages")
TEMP_PAGES = "temp_pages"


def fetch_data(client: httpx.Client | None = None) -> int:
    """
    Fetches all public gists for a user, filters by description prefix,
    and saves the raw content as .rst files while preserving local static pages.

    :param client: Optional httpx.Client for testing purposes.
    :return: Number of gists synced.
    """
    pages_backup = None

    if os.path.exists(PAGES_DIR):
        pages_backup = TEMP_PAGES
        if os.path.exists(pages_backup):
            shutil.rmtree(pages_backup)
        shutil.copytree(PAGES_DIR, pages_backup)

    if os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)
    os.makedirs(CONTENT_DIR)

    if pages_backup and os.path.exists(pages_backup):
        os.makedirs(PAGES_DIR, exist_ok=True)
        shutil.copytree(pages_backup, PAGES_DIR, dirs_exist_ok=True)
        shutil.rmtree(pages_backup)

    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    if client is None:
        with httpx.Client(headers=headers, timeout=30.0) as client:
            return _fetch_gists(client)
    else:
        return _fetch_gists(client)


def _fetch_gists(client: httpx.Client):
    page = 1
    synced_count = 0
    error_count = 0

    print(f"Starting sync for user: {USERNAME}...")

    while True:
        params = {"page": page, "per_page": 100}

        try:
            response = client.get(GIST_API, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(
                f"ERROR: Failed to fetch gists page {page}: {e.response.status_code} - {e.response.text}",
                file=sys.stderr,
            )
            sys.exit(1)
        except httpx.RequestError as e:
            print(
                f"ERROR: Network error fetching gists page {page}: {e}", file=sys.stderr
            )
            sys.exit(1)

        gists = response.json()

        if not gists:
            break

        for gist in gists:
            description = gist.get("description") or ""

            if description.startswith("blog:"):
                files = gist.get("files", {})
                if not files:
                    continue

                file_meta = list(files.values())[0]
                raw_url = file_meta["raw_url"]

                try:
                    content_res = client.get(raw_url)
                    content_res.raise_for_status()
                    content = content_res.text
                except httpx.HTTPStatusError as e:
                    print(
                        f"ERROR: Failed to fetch gist content {gist['id']}: {e.response.status_code} - {e.response.text[:200]}",
                        file=sys.stderr,
                    )
                    error_count += 1
                    continue
                except httpx.RequestError as e:
                    print(
                        f"ERROR: Network error fetching gist content {gist['id']}: {e}",
                        file=sys.stderr,
                    )
                    error_count += 1
                    continue

                filename = f"{gist['id']}.rst"
                filepath = os.path.join(CONTENT_DIR, filename)

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)

                synced_count += 1

        page += 1

    print(f"Finished. Total gists synced: {synced_count}")
    if error_count > 0:
        print(f"Warning: {error_count} gists failed to fetch", file=sys.stderr)

    return synced_count


def fetch_data_cli():
    try:
        count = fetch_data()
        print(f"Synced {count} gists.")
    except SystemExit:
        raise
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    fetch_data_cli()
