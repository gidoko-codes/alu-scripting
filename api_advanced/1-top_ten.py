#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/alu_student)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get("data") or {}
    except (requests.RequestException, ValueError, AttributeError):
        print(None)
        return
    posts = data.get("children")
    if not posts:
        print(None)
        return
    for post in posts[:10]:
        title = (post.get("data") or {}).get("title")
        try:
            print(title)
        except UnicodeEncodeError:
            print(title.encode("ascii", "replace").decode("ascii"))
