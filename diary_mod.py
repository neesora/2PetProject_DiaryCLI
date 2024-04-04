'''
TODO LIST:
1. Finish modEntry func [+]
  1.1 If was wrote nothing, keep last value
2. Add remove func [+]
3. Pair with SQLite
???. Testing and debugging(create module with data for test-cases)
'''
import sqlite3
con = sqlite3.connect('entries.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Entries (date TEXT NOT NULL, entry TEXT NOT NULL, mood TEXT NOT NULL)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_date ON Entries (date)')

class Diary:


    def addEntry(self):
        date = input("Input the date: ")
        entry = input("Input some text: ")
        mood = input("Input the mood: ")
        cur.execute('INSERT INTO Entries VALUES (?, ?, ?);', (date, entry, mood))
        con.commit()

    def searchEntry(self):
        searchKey = input("Input date for search entry: ")
        conc = cur.execute('SELECT ? FROM Entries;', searchKey)
        cur.fetchall()
        print(conc)

    def modEntry(self):
        searchKey = input("Input date for search mod entry: ")
        Entries = cur.fetchall()
        for entryX in Entries:
            if searchKey in entryX:
                date = input("Input new date: ")
                entry = input("Input new entry: ")
                mood = input("Input new mood: ")
                cur.execute('UPDATE Entries SET (date = ?, entry = ?, mood = ?) WHERE searchKey;', (date, entry, mood))
                con.commit()
                break
            else:
                print("This entry doesn't found")

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
        for entry in entries:
            print('All entries out: ', entry)
            break
    
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