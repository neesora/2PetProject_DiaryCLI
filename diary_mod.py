class Diary:

    diary_arr = []

    def addEntry(self):
        date = input("Input the date: ")
        entry = input("Input some text: ")
        mood = input("Input the mood: ")
        entry_dict = {date:'Date', entry:'Entry', mood:'Mood'}
        self.diary_arr.append(entry_dict)
    def searchEntry(searchKey):
        searchKey = input("Input date for search entry: ")
        for searchKey in diary.diary_arr: #seems like wrong searching and doesn't catch the right string
            if searchKey in diary.diary_arr: #another option I can do through transforming list into dict and tryna find through key
                findIndex = diary.diary_arr.index(searchKey)
                print(diary.diary_arr[findIndex])
            else:
                print("This date isn't exist")
    def selector(choice):
        while True:
            print("Choose what do you want. \n 1. Add new entry \n 2. Search entry by date \n 0. Exit program")
            choice = int(input()) #for values in there updating choice should be in while loop.
            if choice == 1:
                diary.addEntry()
            elif choice == 2:
                diary.searchEntry()
            elif choice == 0:
                break
            else:
                print("Choose correct option")
diary = Diary() #create an instance of diary
#diary.addEntry()
diary.selector()
#diary.addEntry(date=input("Input the date: "), entry=input("Input the text: "), mood=input("Input the mood: "))
print("Test", diary.diary_arr)