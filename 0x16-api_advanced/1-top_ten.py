#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """prints the titiles of the first 10 posts"""
    data = requests.get("https://www.reddit.com/r/"
                        + subreddit + "/hot.json?limit=10").json()
    try:
        for title in data["children"]:
            print(title["data"]["title"])
    except Exception as e:
        return None
