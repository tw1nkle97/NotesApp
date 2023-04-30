# notes application with the ability to save / edit / read / add / delete notes. The note must contain an ID, a title, a note body, and a date.

import csv
import datetime


def add_note():
    with open('NotesApp/notes.csv', mode='r') as file:
        reader = csv.DictReader(file)
        last_row = None
        for row in reader:
            last_row = row
        if last_row:
            last_id = int(last_row['id'])
        else:
            last_id = 0
        note_id = last_id + 1
    with open("NotesApp/notes.csv", "a", newline='') as file:
        writer = csv.writer(file, delimiter=',')  # Use the same delimiter for reading and writing
        note_title = input('Заголовок: ')
        note_body = input('Заметка: ')
        note_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        writer.writerow([note_id, note_title, note_body, note_date])


def read_note():
    with open("NotesApp/notes.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')  # Use the same delimiter for reading and writing
        for row in reader:
            print(row)




add_note()
read_note()
