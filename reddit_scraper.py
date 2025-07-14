from dotenv import load_dotenv
import os
import praw
import json
from urllib.parse import urlparse

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username(url):
    return urlparse(url).path.strip('/').split('/')[-1]

def scrape_reddit_user(username):
    try:
        user = reddit.redditor(username)
        _ = user.id  #error is user does not exist
    except Exception as e:
        raise ValueError(f"❌ Could not fetch user: {username}. Reason: {str(e)}")

    data = {"comments": [], "posts": []}


    for comment in user.comments.new(limit=100):
        data["comments"].append({
            "text": comment.body,
            "permalink": f"https://reddit.com{comment.permalink}"
        })

    for post in user.submissions.new(limit=50):
        data["posts"].append({
            "title": post.title,
            "body": post.selftext,
            "permalink": f"https://reddit.com{post.permalink}"
        })

    with open(f'sample_data/{username}_raw.json', 'w') as f:
        json.dump(data, f, indent=2)

    return data
