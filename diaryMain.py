'''
TODO LIST:
5. CLI
6. Redesigne modEntry, delEntry, searchEntry. When you see result, you have choice
 6.1 This row right
 6.2 Show next(less prioritize)
6. Testing through pytest, unittest
7. Simple UI
DESC:
- list, dict, index, class, def(how to working with obj)
- sqlite3: create table, set primary key, insert values, modify them, del row
'''
import sqlite3
import random
from sqlite_utils import Database
from sqlite_utils.db import NotFoundError
from datetime import date

class Diary:
    def __init__(self):
        self.con = Database(sqlite3.connect("Entries.db"))
        self.Entries = self.con["Entries"]

    def createDB(self):
        self.Entries.create({
            "id": int,
            "today": str,
            "entry": str,
            "mood": str,
        }, pk="id", not_null=set())

    def append(self):
        idX = random.randrange(999999)
        today = date.today()
        entry = input("Input some text: ")
        mood = input("Input the mood: ")
        try:
            self.Entries.insert_all([{
                "id": idX,
                "today": today,
                "entry": entry,
                "mood": mood,
            }], pk="id")
        except sqlite3.IntegrityError:
            print("Record already exists with that primary key")

    def search(self, input_word):
        query = f"SELECT * FROM Entries WHERE today LIKE ?"
        cursor = self.con.execute(query, (f"%{input_word}%",))
        row = cursor.fetchone()
        print(row)

    def change(self, searchKey):
        today = date.today()
        entry = input("Input the new entry text: ")
        mood = input("Input new mood: ")
        try:
            self.Entries.upsert({
                "id": searchKey,
                "today": today,
                "entry": entry,
                "mood": mood,
            }, pk="id")
        except NotFoundError:
            print("That entry doesn't exist")

    def remove(self, searchKey):
        try:
            self.Entries.delete(searchKey)
        except NotFoundError:
            print("That entry doesn't exist")

    def test(self):
        for row in self.Entries.rows:
            print('All entries out: ', row)