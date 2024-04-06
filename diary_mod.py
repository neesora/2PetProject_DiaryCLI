'''
TODO LIST:
1. Finish modEntry func [+]
  1.1 If was wrote nothing, keep last value
2. Add remove func [+]
3. Pair with SQLite
???. Testing and debugging(create module with data for test-cases)
'''
import sqlite3
from datetime import date
con = sqlite3.connect('entries.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Entries (today TEXT NOT NULL, entry TEXT NOT NULL, mood TEXT NOT NULL)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_date ON Entries (today)')

class Diary:


    def addEntry(self):
        today = date.today()
        entry = input("Input some text: ")
        mood = input("Input the mood: ")
        cur.execute('INSERT INTO Entries VALUES (?, ?, ?);', (today, entry, mood))
        con.commit()

    def searchEntry(self):
        searchKey = input("Input date for search entry: ")
        cur.execute('SELECT today, entry, mood FROM Entries WHERE today=?', (searchKey,))
        row = cur.fetchone()
    
        if row:
            print('Date: {}\nEntry: {}\nMood: {}'.format(row[0], row[1], row[2]))
        else:
            print('Entry not found')


    def modEntry(self):
        today = input("Input date for search mod entry: ")
        entry = input("Input new entry: ")
        mood = input("Input new mood: ")
        cur.execute('UPDATE Entries SET (today=?, entry=?, mood=?) WHERE today=?', (today, entry, mood))
        con.commit()

    def delEntry(self):
        searchKey = input("Input date for search del entry: ")
        for ind, entryStr in enumerate(self.diary_arr):
            if searchKey in entryStr:
                del self.diary_arr[ind]
                break
            else:
                print("This entry doesn't found")

    def test(self):
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
#diary.sqlite()
diary.selector()
#print("Test", diary.diary_arr)