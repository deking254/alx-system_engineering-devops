#!/usr/bin/python3
import requests
import sys
import csv
print(dir(csv))
"""this is an api call program"""
if __name__ == "__main__":
    i = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(i)
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(i)
    c = 0
    tasks = requests.get(url).json()
    user = requests.get(user_url).json().get("name")
    t = len(tasks)
    for task in tasks:
        if task.get("completed"):
            c = c + 1
    print("Employee {} is done with tasks({}/{}):".format(user, c, t))
    for task in tasks:
        if task.get("completed"):
            print("\t " + task.get("title"))
