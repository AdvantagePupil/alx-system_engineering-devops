#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id)).json()
    todos_response = requests.get(url + "todos", params={"userId": user_id}).json()

    completed_tasks = [t for t in todos_response if t.get("completed")]
    total_tasks = len(todos_response)

    print(f"Employee {user_response.get('name')} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
