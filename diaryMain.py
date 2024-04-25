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

    def addEntry(self, entry, mood):
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

    def searchEntry(self, input_word):
        query = f"SELECT * FROM Entries WHERE today LIKE ?"
        cursor = self.con.execute(query, (f"%{input_word}%",))
        row = cursor.fetchone()
        print(row)

    def modEntry(self, searchKey, entry, mood):
        today = date.today()
        try:
            self.Entries.upsert({
                "id": searchKey,
                "today": today,
                "entry": entry,
                "mood": mood,
            }, pk="id")
        except NotFoundError:
            print("That entry doesn't exist")

    def delEntry(self, searchKey):
        try:
            self.Entries.delete(searchKey)
        except NotFoundError:
            print("That entry doesn't exist")

    def test(self):
        for row in self.Entries.rows:
            print('All entries out: ', row)

    def selector(self):
        while True:
            print("Choose what do you want. \n 1. Add new entry \n 2. Search entry by date \n 3. Modify entry \n 4. Remove entry \n 5. test \n 0. Exit program")
            choice = int(input())
            match choice:
                case 1:
                    self.addEntry()
                case 2:
                    input_word = input("Input search: ")
                    self.searchEntry(input_word)
                case 3:
                    searchKey = input("Input id to edit row: ")
                    self.modEntry(searchKey)
                case 4:
                    searchKey = input("Input id to delete row: ")
                    self.delEntry(searchKey)
                case 5:
                    self.test()
                case 0:
                    break
                case _:
                    print("Choose correct option")
