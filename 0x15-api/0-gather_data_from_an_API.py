#!/usr/bin/python3
"""Saves to-do list information for a given employee ID to a JSON file."""
import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    result = {
        user_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["name"]
            }
            for task in todos
        ]
    }

    with open(f"{user_id}.json", "w") as f:
        json.dump(result, f, indent=4)

    print(f"To-do list for user {user['name']} (ID {user_id}) saved to {user_id}.json")
