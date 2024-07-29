#!/usr/bin/env python3
import requests
import sys

def fetch_employee_and_todos(employee_id):
    """Fetches user and todo items for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user = user_response.json()
    
    # Fetch todos for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()
    
    return user, todos

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        return
    
    employee_id = int(sys.argv[1])
    user, todos = fetch_employee_and_todos(employee_id)
    
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    
    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    main()
