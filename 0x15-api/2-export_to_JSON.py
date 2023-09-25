#!/usr/bin/python3
"""this is an api call program"""
import json
import requests
import sys


if __name__ == "__main__":
    i = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(i)
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(i)
    tasks = requests.get(url).json()
    username = requests.get(user_url).json().get("username")
    user_dict = {i: []}
    for task in tasks:
        t = task.get('title')
        c = task.get('completed')
        new = {"task": t, "completed": c, "username": username}
        user_dict.get(i).append(new)
    j = json.dumps(user_dict)
    with open(i + ".json", mode='w') as fil:
        fil.write(j)
