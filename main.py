import sys
import json
from datetime import datetime
from storage import load_notes, save_notes, load_tasks, save_tasks
from notes import add_note, list_notes, delete_note






def done_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
            return

    print("Task not found.")




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


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task not found.")
        return

    save_tasks(new_tasks)
    print("Task deleted.")





def today_view():
    print("=== TODAY ===\n")

    tasks = load_tasks()
    pending_tasks = [t for t in tasks if not t["done"]]

    print("Tasks:")
    if not pending_tasks:
        print("  No pending tasks.")
    else:
        for task in pending_tasks:
            print(f"  {task['id']}: {task['content']}")

    print("\nRecent Notes:")
    notes = load_notes()

    if not notes:
        print("  No notes found.")
    else:
        for note in notes[-3:]:
            print(f"  {note['id']}: {note['content']}")

# Help
def show_help():
    print("""
Life Manager Commands:

Notes:
  add-note "text"       → Add a new note
  list-notes            → List all notes
  delete-note <id>      → Delete a note

Tasks:
  add-task "text"       → Add a new task
  list-tasks            → List all tasks
  done-task <id>        → Mark task as done
  delete-task <id>      → Delete a task

General:
  today                 → Show today's dashboard
  help                  → Show this help message
""")


# CLI handling
if len(sys.argv) < 2:
    print("Usage: python main.py add-note \"your note\"")
    sys.exit()

command = sys.argv[1]

if command == "add-note":
    content = " ".join(sys.argv[2:])
    add_note(content)

elif command == "delete-note":
    note_id = int(sys.argv[2])
    delete_note(note_id)

elif command == "delete-task":
    task_id = int(sys.argv[2])
    delete_task(task_id)


elif command == "today":
    today_view()


elif command == "done-task":
    task_id = int(sys.argv[2])
    done_task(task_id)

elif command == "list-notes":
    list_notes()

elif command == "add-task":
    content = " ".join(sys.argv[2:])
    add_task(content)

elif command == "list-tasks":
    list_tasks()


elif command == "help":
    show_help()

else:
    print("Unknown command")