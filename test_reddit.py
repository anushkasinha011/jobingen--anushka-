from adapters.reddit import RedditClient

reddit = RedditClient()

posts = reddit.fetch_posts("technology", limit=5)

for post in posts:
    print(post)