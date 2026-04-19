from datetime import datetime
from storage import load_notes, save_notes



id="fixnote1"
def add_note(content):
    notes = load_notes()

    if notes:
        new_id = max(n["id"] for n in notes) + 1
    else:
        new_id = 1

    note = {
        "id": new_id,
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



def delete_note(note_id):
    notes = load_notes()
    new_notes = [n for n in notes if n["id"] != note_id]

    if len(new_notes) == len(notes):
        print("Note not found.")
        return

    save_notes(new_notes)
    print("Note deleted.")