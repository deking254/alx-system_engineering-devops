#!/usr/bin/python3
"""this file handles the titles that are hot"""
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
