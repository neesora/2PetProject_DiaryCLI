class Diary:

    diary_arr = [] 

    def addEntry(self, date, entry, mood):
        entry_dict = {date:'Date', entry:'Entry', mood:'Mood'}
        self.diary_arr.append(entry_dict)
    #def nonStop():
        #asking entry and mood
        #call addEntry

diary = Diary() #create an instance of diary
diary.addEntry(input()) #I must think how to solve it when I try to add
#something this add only "date", but entry and mood not
print("Test", diary.diary_arr)