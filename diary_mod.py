class Diary:

    diary_arr = [] 

    def addEntry(self, date, entry, mood):
        entry_dict = { date:'Date', entry:'Entry', mood:'Mood'} #create dictionary
        self.diary_arr.append(entry_dict)

diary = Diary() #create an instance of diary

diary.addEntry = input() #make for this values will displayed
print("Test", diary.diary_arr)