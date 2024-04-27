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

    def createDB(self):
        self.Entries.create({
            "id": int,
            "today": str,
            "entry": str,
            "mood": str,
        }, pk="id", not_null=set())

    def append(self, entry, mood):
        idX = random.randrange(999999)
        today = date.today()
        try:
            self.Entries.insert_all([{
                "id": idX,
                "today": today,
                "entry": entry,
                "mood": mood,
            }], pk="id")
        except sqlite3.IntegrityError:
            print("Record already exists with that primary key")

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
            print("That entry doesn't exist")

    def remove(self, remove):
        try:
            self.Entries.delete(remove)
        except NotFoundError:
            print("That entry doesn't exist")

    def test(self):
        for row in self.Entries.rows:
            print('All entries out: ', row)
#def idGenerator(self, id):
    #create id from 0.
    #check which number last
    #+=1 for new entry