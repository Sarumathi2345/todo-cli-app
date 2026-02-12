import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, description, priority="Medium"):
    tasks.append({
        "description": description,
        "done": False,
        "priority": priority
    })
    save_tasks(tasks)
    print(f"Added: {description} (Priority: {priority})")

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            priority = task.get("priority", "Medium")
            print(f"{i}. [{status}] ({priority}) {task['description']}")

def delete_task(tasks, index):
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['description']}")
    except IndexError:
        print("Invalid task number.")

def mark_done(tasks, index):
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")

def search_tasks(tasks, keyword):
    results = [task for task in tasks if keyword.lower() in task["description"].lower()]
    if not results:
        print("No matching tasks found.")
    else:
        print("\nSearch Results:")
        for i, task in enumerate(results):
            status = "✓" if task["done"] else "✗"
            priority = task.get("priority", "Medium")
            print(f"[{status}] ({priority}) {task['description']}")

def clear_completed(tasks):
    tasks[:] = [task for task in tasks if not task["done"]]
    save_tasks(tasks)
    print("Cleared all completed tasks.")

def main():
    tasks = load_tasks()
    print("Welcome to CLI Todo App")
    print("Commands:")
    print(" add <task> [priority]")
    print(" list")
    print(" delete <index>")
    print(" done <index>")
    print(" search <keyword>")
    print(" clear")
    print(" exit")

    while True:
        command = input("\n> ").strip().split()
        if not command:
            continue

        if command[0] == "add" and len(command) > 1:
            desc = " ".join(command[1:-1]) if len(command) > 2 else command[1]
            priority = command[-1].capitalize() if len(command) > 2 else "Medium"
            if priority not in ["High", "Medium", "Low"]:
                priority = "Medium"
            add_task(tasks, desc, priority)

        elif command[0] == "list":
            list_tasks(tasks)

        elif command[0] == "delete" and len(command) > 1:
            try:
                delete_task(tasks, int(command[1]))
            except ValueError:
                print("Please enter a valid number.")

        elif command[0] == "done" and len(command) > 1:
            try:
                mark_done(tasks, int(command[1]))
            except ValueError:
                print("Please enter a valid number.")

        elif command[0] == "search" and len(command) > 1:
            keyword = " ".join(command[1:])
            search_tasks(tasks, keyword)

        elif command[0] == "clear":
            clear_completed(tasks)

        elif command[0] == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
