
# note

import os
import pickle

the_notes = []

#get the list of notes
def get_notes():
    global the_notes
    if os.path.exists("notes.pkl"):
        with open("notes.pkl","rb") as f:
            the_notes = pickle.load(f)
    return the_notes

# add a note to the list of notes
def add_note(note):
    global the_notes
    if os.path.exists("notes.pkl"):
        with open("notes.pkl","rb") as f:
            the_notes = pickle.load(f)
    print("the initial notes")
    print("the notes")
    the_notes.append(note)
    print("the notes")
    print(the_notes)
    with open("notes.pkl","wb") as f:
        pickle.dump(the_notes, f)