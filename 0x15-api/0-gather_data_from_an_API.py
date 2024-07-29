#!/usr/bin/env python3
# This script fetches and prints the details of completed tasks for a specific employee.

import requests
from sys import argv


def get_user_and_todos(user_id):
    """Fetches user and todo items for a given user ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{user_id}")
    user = user_response.json()
    
    # Fetch todos for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": user_id})
    todos = todos_response.json()
    
    return user, todos


def main():
    if len(argv) < 2:
        print("Usage: python script.py <employee_id>")
        return
    
    user_id = argv[1]
    user, todos = get_user_and_todos(user_id)
    
    completed_tasks = [task["title"] for task in todos if task.get("completed")]
    
    print(f"Employee {user['name']} is done with tasks ({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    main()
