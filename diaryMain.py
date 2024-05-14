'''
TODO LIST:
1.1 Make better view
2. Simple UI [TBC]
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

    def change(self, today, row):
        query = f"SELECT * FROM Entries WHERE today = '{today}' ORDER BY id"
        cursor = self.con.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            click.echo(f"Founded entry: \n Date: {row[1]} Entry: {row[2]} Mood: {row[3]}")
            if click.confirm("This is right row?"):
                answer = click.prompt("Input d or c for deletion or changing", type=str)
                if answer == "c":
                    self.update_entry(row[0], today)
                elif answer == "d":
                    self.remove(row[0])
                break
            else:
                self.number += 1
        return None
    def update_entry(self, id, today):
        entry = click.prompt("Input new entry", type=str)
        mood = click.prompt("Input new mood", type=str)
        self.Entries.upsert({
            "id": id,
            "today": today,
            "entry": entry,
            "mood": mood,
        }, pk="id")

    def remove(self, id):
            self.Entries.delete(id)