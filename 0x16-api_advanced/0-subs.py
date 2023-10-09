#!/usr/bin/python3
"""the subscribers of the subreddit"""
import urllib.request as urllib
import json

def number_of_subscribers(subreddit):
    """returns the no of subscribers to subreddit and 0 if nothing"""
    CLIENT_ID = "u13OXnhDSKr0SR42N1-L5WqVKJ3KuQ"
    TYPE = "code"
    RANDOM_STRING = "were"
    SCOPE_STRING = "[wikiread]"
    URI = "http://127.0.0.1:65010/authorize_callback"
    DURATION = "permanent"
    urllib.urlopen("https://www.reddit.com/api/v1/authorize?client_id=" + CLIENT_ID + "&response_type=" + TYPE + "&state=" + 
            RANDOM_STRING + "&redirect_uri=" + URI + "&duration=" 
            + DURATION + "&scope=" + SCOPE_STRING)
    if subreddit:
        data = urllib.urlopen("https://api.reddit.com/r/" + subreddit + "/about")
        tr = json.loads(data.read())
        return tr["data"]["subscribers"]
