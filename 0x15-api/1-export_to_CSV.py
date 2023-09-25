#!/usr/bin/python3
"""this is an api call program"""
import csv
import requests
import sys

if __name__ == "__main__":
    i = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(i)
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(i)
    tasks = requests.get(url).json()
    username = requests.get(user_url).json().get("username")
    t = len(tasks)
    list_outer = []
    list_inner = []
    for task in tasks:
        list_inner.append(i)
        list_inner.append(username)
        list_inner.append(task.get("completed"))
        list_inner.append(task.get("title"))
        list_outer.append(list_inner)
        list_inner = []
    with open(i + ".csv", mode='w', newline='') as file:
        wr = csv.writer(file, "unix")
        for row in list_outer:
            wr.writerow(row)
