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

# CLI handling
if len(sys.argv) < 2:
    print("Usage: python main.py add-note \"your note\"")
    sys.exit()

command = sys.argv[1]

if command == "add-note":
    content = " ".join(sys.argv[2:])
    add_note(content)

else:
    print("Unknown command")