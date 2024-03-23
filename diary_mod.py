class Diary:

    diary_arr = []

    def addEntry(self):
        date = input("Input the date: ")
        entry = input("Input some text: ")
        mood = input("Input the mood: ")
        entry_dict = {date:'Date', entry:'Entry', mood:'Mood'}
        self.diary_arr.append(entry_dict)
    def selector(self):
        print("Choose what do you want. \n 1. Add new entry \n 0. Exit program")
        choice = input()
        while True:
            if choice == "1":
                diary.addEntry()#stack in eternal cycle
                #self.selector() re-call func
            elif choice == "0":
                break
            else:
                print("Choose correct option")
diary = Diary() #create an instance of diary
#diary.addEntry()
diary.selector()
#diary.addEntry(date=input("Input the date: "), entry=input("Input the text: "), mood=input("Input the mood: "))
print("Test", diary.diary_arr)