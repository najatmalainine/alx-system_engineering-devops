#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import requests
import sys


def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    return employee_name, todo_data


def display_todo_progress(employee_name, todo_data):
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(done_tasks)}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as the employee ID.")
        sys.exit(1)

    employee_name, todo_data = fetch_employee_data(employee_id)
    display_todo_progress(employee_name, todo_data)
