import sys
import json
import os
from datetime import datetime


## Loading and Saving Tasks

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


## Adding a Task
def add_task(description):
    tasks = load_tasks()
    new_id =max([task['id'] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully with ID {new_id}.")


## Updating a Task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")


## Deleting a Task
def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return
    print(f"Task {task_id} not found")


## Changing Task Status
def mark_task_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")


## Listing Tasks
def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        filtered_tasks = [task for task in tasks if task['status'] == status_filter]
        if not filtered_tasks:
            print(f"No tasks with status '{status_filter}' found")
            return
        tasks = filtered_tasks
    
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created: {task['createdAt']}")
        print(f"Last Updated: {task['updatedAt']}")
        print("-" * 30)


## Main Functionality | Handling Command-Line Arguments
def print_usage():
    print("Usage:")
    print("  task-cli add \"Task description\"")
    print("  task-cli update <task_id> \"New description\"")
    print("  task-cli delete <task_id>")
    print("  task-cli mark-in-progress <task_id>")
    print("  task-cli mark-done <task_id>")
    print("  task-cli list")
    print("  task-cli list todo|in-progress|done")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == 'add' and len(sys.argv) >= 3:
        description = ' '.join(sys.argv[2:])
        add_task(description)
    elif command == 'update' and len(sys.argv) >= 4:
        try:
            task_id = int(sys.argv[2])
            new_description = ' '.join(sys.argv[3:])
            update_task(task_id, new_description)
        except ValueError:
            print("Invalid task ID")
    elif command == 'delete' and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Invalid task ID")
    elif command == 'mark-in-progress' and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_task_status(task_id, 'in-progress')
        except ValueError:
            print("Invalid task ID")
    elif command == 'mark-done' and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_task_status(task_id, 'done')
        except ValueError:
            print("Invalid task ID")
    elif command == 'list' and len(sys.argv) == 2:
        list_tasks()
    elif command == 'list' and len(sys.argv) == 3:
        status_filter = sys.argv[2].lower()
        if status_filter in ['todo', 'in-progress', 'done']:
            list_tasks(status_filter)
        else:
            print("Invalid status filter. Use 'todo', 'in-progress', or 'done'")
    else:
        print_usage()

if __name__ == '__main__':
    main()

