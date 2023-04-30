# notes application with the ability to save / edit / read / add / delete notes. The note must contain an ID, a title, a note body, and a date.

import csv
import datetime


def add_note():
    fieldnames = ['id', 'Title', 'Body', 'Date&Time']
    with open('NotesApp/notes.csv', mode='r') as file:
        reader = csv.DictReader(file, fieldnames=fieldnames, delimiter=';')
        last_row = None
        for row in reader:
            last_row = row
        if last_row:
            last_id = int(last_row['id'])
        else:
            last_id = 0
        note_id = last_id + 1
    with open("NotesApp/notes.csv", "a", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        note_title = input('Заголовок: ')
        note_body = input('Заметка: ')
        note_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        writer.writerow([note_id, note_title, note_body, note_date])


def read_note():
    with open("NotesApp/notes.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)


def edit_note():
    note_id = input('Введите ID заметки, которую хотите отредактировать: ')

    notes = []
    with open("NotesApp/notes.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            notes.append(row)

    found = False
    for note in notes:
        if note[0] == note_id:
            found = True
            print(f'Заголовок: {note[1]}')
            print(f'Тело заметки: {note[2]}')
            new_title = input('Введите новый заголовок (оставьте пустым, чтобы оставить текущий): ')
            new_body = input('Введите новое тело заметки (оставьте пустым, чтобы оставить текущее): ')
            if new_title:
                note[1] = new_title
            if new_body:
                note[2] = new_body
            break

    if not found:
        print('Заметка с таким ID не найдена.')
    else:
        with open("NotesApp/notes.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for note in notes:
                writer.writerow(note)

        print('Заметка успешно отредактирована.')


def delete_note():
    note_id = input('Введите ID заметки, которую хотите удалить: ')

    notes = []
    with open("NotesApp/notes.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            notes.append(row)

    found = False
    for note in notes:
        if note[0] == note_id:
            found = True
            notes.remove(note)
            break

    if not found:
        print('Заметка с таким ID не найдена.')
    else:
        with open("NotesApp/notes.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for note in notes:
                writer.writerow(note)

        print('Заметка удалена')


def main_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Читать заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Введите номер пункта: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            read_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")


main_menu()