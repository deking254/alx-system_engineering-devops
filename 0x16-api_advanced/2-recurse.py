#!/usr/bin/python3
"""this file handles the titles that are hot"""
import requests


def recurse(subreddit, hot_list=[]):
    """prints the titiles of the first 10 posts"""
    CLIENT_ID = "u13OXnhDSKr0SR42N1-L5WqVKJ3KuQ"
    TYPE = "code"
    RANDOM_STRING = "were"
    SCOPE_STRING = "[wikiread]"
    URI = "http://127.0.0.1:65010/authorize_callback"
    DURATION = "permanent"
    requests.get("https://www.reddit.com/api/v1/authorize?client_id="
                 + CLIENT_ID
                 + "&response_type=" + TYPE + "&state=" +
                 RANDOM_STRING + "&redirect_uri=" + URI + "&duration="
                 + DURATION + "&scope=" + SCOPE_STRING)
    data = requests.get("https://api.reddit.com/r/"
                        + subreddit + "/hot?limit=10").json()
    try:
        i = 0
        for title in data["data"]["children"]:
            print(title["data"]["title"])
            i = i + 1
            if i == 9:
                break
    except Exception as e:
        print(None)
