import feedparser
import os
import re

# Inputs are passed as environment variables
FEED_URL = os.getenv('INPUT_FEED_URL')
README_PATH = os.getenv('INPUT_README_PATH', 'README.md')
MAX_POSTS = int(os.getenv('INPUT_MAX_POSTS', '5'))

# Fetch posts from blog feed url
def fetch_posts():
    feed = feedparser.parse(FEED_URL)
    posts = []
    for entry in feed.entries[:MAX_POSTS]:
        title = entry.title
        link = entry.link
        # You can customize the format here
        posts.append(f"- [{title}]({link})")
    return "\n".join(posts)

# Update readme
def update_readme(posts_markdown):
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the markers
    start_marker = "<!-- BLOGPOST-LIST:START -->"
    end_marker = "<!-- BLOGPOST-LIST:END -->"

    # Regex to replace content between markers
    pattern = f"{start_marker}(.*?){end_marker}"
    replacement = f"{start_marker}\n{posts_markdown}\n{end_marker}"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    posts = fetch_posts()
    update_readme(posts)
    print("README updated successfully.")
  
