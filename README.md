# Simple GitHub action to update your profile with latest blog posts
This is a very simple action. You just need to specify your blog's RSS url and that's it.
You can set the number of posts to be shown, but even that's optional (default 5 posts).
Go ahead, get started using it! 😊

## 📌 Goal
Automatically update your GitHub profile `README.md` with your latest blog posts using:  
👉 `maloymanna/actions-blogpost-update@v1`  

## ✅ Prerequisites

1. You have a GitHub profile repository.
   - The repository name must be exactly your GitHub username e.g. if your username is `jill`, the repo must be `jill/jill`
2. The repository must contain a `README.md`
3. Your blog must expose an RSS/Atom feed URL. For example, Wordpress usually adds `feed` at the end of the blog URL like `https://biguru.wordpress.com/feed`, whereas Hugo sites usually add `index.xml` at the end of the blog URL like `https://maloymanna.github.io/index.xml`

## 👣 Step-by-Step Setup

### 1. Add Placeholders in Your `README.md`
Open your profile repo’s `README.md` and add markers where posts should appear:  
```markdown
<!-- BLOGPOST-LIST:START -->
<!-- BLOGPOST-LIST:END -->
```
The `<!-- ` and ` -->` ensures your README.md treats these as HTML comments, so that your profile stays perfect even if your blog feed has errors.  
The action will automatically replace everything between these markers with your latest blog posts.  
Commit and push.
### 2. Create GitHub Action Workflow
Inside your profile repository, create this file:  
```
.github/workflows/blog-posts.yml
```
Create the folder `.github` and the sub-folder `workflows` within it, if these do not exist, before creating the `blog-posts.yml` file.
Paste witin it:  
```yaml
name: Update latest blog posts

on:
  schedule:
    - cron: "0 */6 * * *"   # Runs every 6 hours
  workflow_dispatch:        # Allows manual trigger

jobs:
  update-readme-with-blog:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Update README with latest blog posts
        uses: maloymanna/actions-blogpost-update@v1
        with:
          feed_url: "https://yourblog.com/rss.xml"

      - name: Commit and push changes
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"
          git add README.md
          git diff --quiet && git diff --staged --quiet || git commit -m "Update latest blog posts"
          git push
```
Replace `https://yourblog.com/rss.xml` with your actual RSS feed URL.  
Commit and push.
### 3. Enable Workflow Permissions (Important)
Go to: `Repo → Settings → Actions → General`  
Under `Workflow permissions`, select:  
    ✅ `Read and write permissions`  
Then click `Save`.  
Without these permissions, the action cannot push changes.  
### 4. Trigger your workflow
Trigger your workflow if you don't want to wait for the scheduled run (6 hours, unless you changed the cron setting in the workflow `blog-posts.yml` 😉)  
Go to:
  ```
  Actions → Update latest blog posts → Run workflow
  ```
After it runs successfully, your README will update automatically.  
If it works for you, please star this repo. 😊  
### 5. Optional Configuration
If you wish to modify the number of latest blog posts, update the workflow step in your `blog-posts.yml`.  
It should look like below, e.g. if you wish to display latest 7 posts instead of the default 5:
```yaml
- name: Update README with latest blog posts
  uses: maloymanna/actions-blogpost-update@v1
  with:
    feed_url: "https://yourblog.com/rss.xml"
    max_posts: 7
```
To modify how often the action runs, you only need to change the `cron` expression in the workflow.  
Examples:  
Run every hour: `cron: "0 * * * *"`  
Run every 3 hours: `cron: "0 */3 * * *"`  
Run every 12 hours: `cron: "0 */12 * * *"`  
Run once per day: `cron: "0 0 * * *"`  
If you liked the action, don't forget to give it a star! ⭐
