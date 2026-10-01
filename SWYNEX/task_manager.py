import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "task": task
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        print(task["id"], "-", task["task"])


def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Invalid ID! Please enter a number.")
