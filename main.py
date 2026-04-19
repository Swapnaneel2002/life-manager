import sys
import json
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(content):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "content": content,
        "created_at": str(datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Note added.")

def list_notes():
    notes = load_notes()

    if not notes:
        print("No notes found.")
        return

    for note in notes:
        print(f"{note['id']}: {note['content']}")



TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(content):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "content": content,
        "done": False,
        "created_at": str(datetime.now())
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✔" if task["done"] else "✘"
        print(f"{task['id']}: [{status}] {task['content']}")



# CLI handling
if len(sys.argv) < 2:
    print("Usage: python main.py add-note \"your note\"")
    sys.exit()

command = sys.argv[1]

if command == "add-note":
    content = " ".join(sys.argv[2:])
    add_note(content)

elif command == "list-notes":
    list_notes()

elif command == "add-task":
    content = " ".join(sys.argv[2:])
    add_task(content)

elif command == "list-tasks":
    list_tasks()

else:
    print("Unknown command")