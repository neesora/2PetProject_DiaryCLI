class Diary:

    diary_arr = [] 

    def addEntry(self, date, entry, mood):
        entry_dict = { date:'Date', entry:'Entry', mood:'Mood'} #create dictionary
        self.diary_arr.append(entry_dict)

diary = Diary() #create an instance of diary

entry_add = diary.addEntry('12 march', 'I do anal', 'Fine')
print("Test", diary.diary_arr)
#next step I should add entry by input