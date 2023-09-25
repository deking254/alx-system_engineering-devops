#!/usr/bin/python3
"""this is an api call program"""
import json
import requests
import sys


if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(user_url).json()
    url = 'https://jsonplaceholder.typicode.com/todos'
    tasks = requests.get(url).json()
    ids = []
    holder_dict = {}
    usernames = {}
    for user in users:
        usernames.update({user.get("id"): user.get("username")})
        ids.append(user.get("id"))

    for usr in ids:
        new_dict = {usr: []}
        for task in tasks:
            if task.get("userId") == usr:
                u = usernames.get(usr)
                t = task.get('title')
                c = task.get('completed')
                ta = "task"
                co = "completed"
                us = "username"
                new_dict.get(usr).append({ta: t, co: c, us: u})
        holder_dict.update(new_dict)
    j = json.dumps(holder_dict)
    with open("todo_all_employees.json", mode='w') as fil:
        fil.write(j)
