'''
TODO LIST:
5. CLI [+]
6. Redesigne modEntry, delEntry, searchEntry. When you see result, you have choice
 6.1 This row right [+]
 6.2 Show next(less prioritize) [+]
7. Apply somehow search into modify functions
8. Testing through pytest, unittest [TBC]
9. Simple UI
DESC:
- list, dict, index, class, def(how to working with obj)
- sqlite3: create table, set primary key, insert values, modify them, del row
'''
import sqlite3
import click
from sqlite_utils import Database
from sqlite_utils.db import NotFoundError
from datetime import date

class Diary:
    def __init__(self):
        self.con = Database(sqlite3.connect("Entries.db"))
        self.Entries = self.con["Entries"]
        self.number = 0

    def idGenerator(self, id):
        query = "SELECT * FROM Entries ORDER BY id DESC LIMIT 1;"
        cursor = self.con.execute(query)
        cursor.execute("SELECT COUNT(*) FROM Entries")
        if cursor.fetchone()[0] > 0:
            query = "SELECT * FROM Entries ORDER BY id DESC LIMIT 1;"
            cursor = self.con.execute(query)
            last_id = cursor.fetchone()[0]
            id = last_id + 1
            return id
        else:
            id = 0
            return id

    def createDB(self):
        self.Entries.create({
            "id": int,
            "today": str,
            "entry": str,
            "mood": str,
        }, pk="id", not_null=set())

    def append(self, entry, mood):
        self.idX = Diary.idGenerator(self, id="")
        today = date.today()
        try:
            self.Entries.insert_all([{
                "id": self.idX,
                "today": today,
                "entry": entry,
                "mood": mood,
            }], pk="id")
        except sqlite3.IntegrityError:
            word = "Error"
            return word

    def search(self, today, answer, row):
        query = f"SELECT * FROM Entries WHERE today = '{today}' ORDER BY id"
        cursor = self.con.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            click.echo(f"Founded entry: \n Date: {row[1]} Entry: {row[2]} Mood: {row[3]}")
            answer = click.prompt("Is this the correct entry? (Yes/No)", type=str)
            if answer.lower() == "yes":
                return row
            else:
                self.number += 1
        return None

    def change(self, today, entry, mood):
        row = searchMethod.picker(row="")
        #here func search with option next row by prioritize or stay
        try:
            self.Entries.upsert({
                "id": row[0],
                "today": today,
                "entry": entry,
                "mood": mood,
            }, pk="id")
        except NotFoundError:
            word = "Error"
            return word

    def remove(self, remove):
        try:
            self.Entries.delete(remove)
        except NotFoundError:
            word = "Error"
            return word

    def test(self, row):
        for row in self.Entries.rows:
            return row
'''
this class include:
*** Function for searching and selection excpect row
*** Function for searching and then pick up row for editing
'''
class searchMethod:
    def picker(self, row):
        today = click.prompt("Type day for searching.", type=str)
        query = f"SELECT * FROM Entries WHERE today = '{today}' ORDER BY id"
        cursor = self.con.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            click.echo(f"Founded entry: \n Date: {row[1]} Entry: {row[2]} Mood: {row[3]}")
            answer = click.prompt("Is this the correct entry? (Yes/No)", type=str)
            if answer.lower() == "yes":
                return row
            else:
                break