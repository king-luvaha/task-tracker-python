# Task Tracker CLI - README

## Overview

Task Tracker CLI is a simple command-line application for managing your tasks. It allows you to add, update, delete, and track the status of tasks (todo, in-progress, done). All tasks are stored in a JSON file for persistence between sessions.

Project URL: https://github.com/king-luvaha/task-tracker-python

## Features

- Add new tasks with descriptions
- Update existing tasks
- Delete tasks
- Mark tasks as "in-progress" or "done"
- List all tasks or filter by status
- Automatic tracking of creation and modification timestamps
- Persistent storage in JSON format

## Prerequisites

- Python 3.x installed on your system

## Installation

1. **Download the application**:
   - Copy the `task-cli.py` file to your desired directory

2. **Make the script executable (optional for Linux/Mac)**:
   ```bash
   chmod +x task-cli.py
   ```

3. **Create an alias (optional for easier access)**:
   - For Linux/Mac:
     ```bash
     echo 'alias task-cli="python3 /path/to/task-cli.py"' >> ~/.bashrc
     source ~/.bashrc
     ```
   - For Windows (add to your PowerShell profile):
     ```powershell
     function task-cli { python C:\path\to\task-cli.py $args }
     ```

## Usage

### Basic Commands

```
task-cli [command] [arguments]
```

### Available Commands

#### 1. Add a new task
```
task-cli add "Task description"
```
Example:
```bash
task-cli add "Buy groceries"
```
Output:
```
Task added successfully (id: 1)
```

#### 2. Update a task
```
task-cli update <task_id> "New description"
```
Example:
```bash
task-cli update 1 "Buy groceries and cook dinner"
```
Output:
```
Task 1 updated successfully
```

#### 3. Delete a task
```
task-cli delete <task_id>
```
Example:
```bash
task-cli delete 1
```
Output:
```
Task 1 deleted successfully
```

#### 4. Mark task as in progress
```
task-cli mark-in-progress <task_id>
```
Example:
```bash
task-cli mark-in-progress 2
```
Output:
```
Task 2 marked as in-progress
```

#### 5. Mark task as done
```
task-cli mark-done <task_id>
```
Example:
```bash
task-cli mark-done 2
```
Output:
```
Task 2 marked as done
```

#### 6. List tasks
```
task-cli list [status_filter]
```
Available status filters: `todo`, `in-progress`, `done`

Examples:
```bash
# List all tasks
task-cli list

# List only todo tasks
task-cli list todo

# List in-progress tasks
task-cli list in-progress

# List completed tasks
task-cli list done
```

Sample output:
```
ID: 1
Description: Buy groceries
Status: todo
Created: 2023-05-15T14:30:00.123456
Last Updated: 2023-05-15T14:30:00.123456
------------------------------
ID: 2
Description: Finish project
Status: in-progress
Created: 2023-05-14T10:15:00.654321
Last Updated: 2023-05-15T09:45:00.987654
------------------------------
```

## Data Storage

All tasks are stored in a JSON file named `tasks.json` in the same directory as the script. The file is automatically created when you add your first task.

Sample data structure:
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2023-05-15T14:30:00.123456",
    "updatedAt": "2023-05-15T14:30:00.123456"
  },
  {
    "id": 2,
    "description": "Finish project",
    "status": "in-progress",
    "createdAt": "2023-05-14T10:15:00.654321",
    "updatedAt": "2023-05-15T09:45:00.987654"
  }
]
```

## Troubleshooting

1. **Python not found**:
   - Ensure Python 3 is installed
   - Try using `python3` instead of `python` in your commands

2. **Permission denied**:
   - On Linux/Mac, run `chmod +x task-cli.py` to make the script executable

3. **Task not found**:
   - Verify the task ID exists by listing all tasks first

4. **JSON file corruption**:
   - If `tasks.json` becomes corrupted, you can safely delete it (all tasks will be lost)

## License

This project is open-source and free to use under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Support

For any issues or feature requests, please open an issue on the GitHub repository (if available) or contact the maintainer directly.
