'''
TODO LIST:
1. Finish modEntry func [+]
  1.1 If was wrote nothing, keep last value[]
2. Add remove func [+]
3. Pair with SQLite [+]
4. Bugs: when I'm add entry it's add Null instead of exist value.
???. Add more than 1 entry per day
5. CLI
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
con = Database(sqlite3.connect("Entries.db"))
Entries = con["Entries.db"]
#con = sqlite3.connect('entries.db')
#cur = con.cursor()
#cur.execute('CREATE TABLE IF NOT EXISTS Entries (today TEXT PRIMARY KEY NOT NULL, entry TEXT NOT NULL, mood TEXT NOT NULL)')

class Diary:


    def addEntry(self):
        idX = random.randrange(999999)
        today = date.today()
        entry = input("Input some text: ")
        mood = input("Input the mood: ")
        con["Entries.db"].insert_all([{
                "id": idX,
                "today": today,
                "entry": entry,
                "mood": mood,
        }])

    def searchEntry(self): #it isn't working
        today = input("Input date for search entries by day: ")
        for row in con["Entries.db"].rows_where("today"):
            print(row)

    def modEntry(self):
        today = date.today()
        searchKey = input("Input id to edit row: ")
        try:
            con["Entries.db"].get(searchKey) 
            entry = input("Input the new entry text: ")
            mood = input("Input new mood: ")
            con["Entries.db"].upsert({
                    "id": searchKey,
                    "today": today,
                    "entry": entry,
                    "mood": mood,
            }, pk="id")
        except NotFoundError:
            print("That's entry doesn't exist")

    def delEntry(self):
        searchKey = input("Input date for delete entry: ")
        cur.execute('SELECT today, entry, mood FROM Entries WHERE today=?', (searchKey,))
        row = cur.fetchone()
        if row != None:
            today = searchKey
            cur.execute('DELETE FROM entries WHERE (today=?)', (today,))
            con.commit()
        else:
            print('Entry not found.')

    def createDB(self):
        Entries.create({
            "id": int,
            "today": str,
            "entry": str,
            "mood": str,
        }, pk="id", not_null=set())

    def test(self): #i must rewrite it
        cur.execute('SELECT * FROM Entries')
        entries = cur.fetchall()
        print('All entries out: ', entries)
            
    
    def selector(choice):
        while True:
            print("Choose what do you want. \n 1. Add new entry \n 2. Search entry by date \n 3. Modify entry \n 4. Remove entry \n 5. test \n 0. Exit program")
            choice = int(input())
            match choice: 
                case 1:
                    diary.addEntry()
                case 2:
                    diary.searchEntry()
                case 3:
                    diary.modEntry()
                case 4:
                    diary.delEntry()
                case 5:
                    diary.test()
                case 0:
                    con.commit()
                    con.close()
                    break
                case _:
                    print("Choose correct option")

diary = Diary() #create an instance of diary
diary.selector()