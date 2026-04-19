from datetime import datetime
from storage import load_tasks, save_tasks



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

def done_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
            return

    print("Task not found.")    
