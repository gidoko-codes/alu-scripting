#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the keywords found in hot post titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    # number of times each (lowercase) keyword appears in word_list
    weights = {}
    for word in word_list:
        word = word.lower()
        weights[word] = weights.get(word, 0) + 1

    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        for token in title.lower().split():
            if token in weights:
                counts[token] = counts.get(token, 0) + weights[token]

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    for word, total in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
