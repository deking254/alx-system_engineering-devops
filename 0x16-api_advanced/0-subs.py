#!/usr/bin/python3
"""the subscribers of the subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the no of subscribers to subreddit and 0 if nothing"""
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
    if subreddit:
        data = requests.get("https://api.reddit.com/r/"
                            + subreddit + "/about")
        try:
            tr = data.json().get("data")
        except Exception as e:
            return 0
        if tr:
            return tr["subscribers"]
        else:
            return 0
    else:
        return 0
