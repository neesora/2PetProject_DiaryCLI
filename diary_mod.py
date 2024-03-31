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
class Diary:

    diary_arr = []

    def addEntry(self):
        date = input("Input the date: ")
        entry = input("Input some text: ")
        mood = input("Input the mood: ")
        entry_dict = {date:'Date', entry:'Entry', mood:'Mood'}
        self.diary_arr.append(entry_dict)
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
    def sqlite(self):
        cur = con.cursor()
        cur.executemany(self.diary_arr)      
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
diary.selector()
print("Test", diary.diary_arr)