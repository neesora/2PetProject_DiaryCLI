'''
TODO LIST:
5. CLI [+]
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

    def idGenerator(self, id):
        query = "SELECT * FROM Entries ORDER BY id DESC LIMIT 1;"
        cursor = self.con.execute(query)
        last_id = cursor.fetchone()[0]
        id = last_id + 1
        return id

    def createDB(self):
        self.Entries.create({
            "id": int,
            "today": str,
            "entry": str,
            "mood": str,
        }, pk="id", not_null=set())

    def append(self, entry, mood):
        self.idX = Diary.idGenerator(self, 0)
        today = date.today()
        try:
            self.Entries.insert_all([{
                "id": self.idX,
                "today": today,
                "entry": entry,
                "mood": mood,
            }], pk="id")
        except sqlite3.IntegrityError:
            return "Error"

    def search(self, search):
        query = f"SELECT * FROM Entries WHERE today LIKE ?"
        cursor = self.con.execute(query, (f"%{search}%",))
        row = cursor.fetchone()
        return row

    def change(self, search, entry, mood):
        today = date.today()
        try:
            self.Entries.upsert({
                "id": search,
                "today": today,
                "entry": entry,
                "mood": mood,
            }, pk="id")
        except NotFoundError:
            return "Error"

    def remove(self, remove):
        try:
            self.Entries.delete(remove)
        except NotFoundError:
            return "Error"

    def test(self):
        for row in self.Entries.rows:
            print('All entries out: ', row)