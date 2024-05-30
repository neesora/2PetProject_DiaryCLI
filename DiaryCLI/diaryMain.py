import sqlite3
import click
from sqlite_utils import Database
from datetime import date

class Diary:
    def __init__(self):
        self.con = Database(sqlite3.connect("Entries.db"))
        self.Entries = self.con["Entries"]
        self.number = 0

    def assignment_ID(self, id): #need for append function and assign ID = pk
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

    def create_DB(self): #use only once when Entries.db isn't exist
        self.Entries.create({
            "id": int,
            "today": str,
            "entry": str,
            "mood": str,
        }, pk="id", not_null=set())

    def append(self, entry, mood): #append new row in Entries.db with id+1 from last
        self.idX = Diary.assignment_ID(self, id="")
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

    def search(self, today, answer, row): #searching row by date in format dd-mm-yyyy
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

    def change(self, today, row): #function for editing rows
        query = f"SELECT * FROM Entries WHERE today = '{today}' ORDER BY id" #selecting all row include date in format dd-mm-yyyy
        cursor = self.con.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            click.echo(f"Founded entry: \n Date: {row[1]} Entry: {row[2]} Mood: {row[3]}")
            if click.confirm("This is right row?"): #select certain row for editing
                answer = click.prompt("Input [d/C] for deletion or changing", type=str)
                if answer == "c": #editing selected row: attribute entry and mood
                    self.update_entry(row[0], today)
                elif answer == "d": #deleting selected row
                    self.remove_entry(row[0])
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

    def remove_entry(self, id):
            self.Entries.delete(id)