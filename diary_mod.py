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
        for entry in self.diary_arr: #that's brute entries
            if searchKey in entry:
                print(entry)
                break
            else:
                print("This entry doesn't found")

    def modEntry(self):
        searchKey = input("Input date for search mod entry: ")
        for ind, entryStr in enumerate(self.diary_arr):
            if searchKey in entryStr:
                date = input("Input new date: ")
                entry = input("Input new entry: ")
                mood = input("Input new mood: ")
                entry_dict = {date:"Date", entry:"Entry", mood:"Mood"}
                self.diary_arr[ind] = entry_dict
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

    #def sqlite():
    
    def selector(choice):
        while True:
            print("Choose what do you want. \n 1. Add new entry \n 2. Search entry by date \n 3. Modify entry \n 4. Remove entry \n 0. Exit program")
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
                case 0:
                    diary.sqlite()
                    break
                case _:
                    print("Choose correct option")

diary = Diary() #create an instance of diary
#diary.sqlite()
diary.selector()
#print("Test", diary.diary_arr)