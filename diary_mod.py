class Diary:

    diary_arr = [] 

    def addEntry(self, entry):
        entry_dict = {entry:'Entry'} #create dictionary
        self.diary_arr.append(entry_dict)

diary = Diary() #create an instance of diary

entry_add = diary.addEntry('123123')
print("Test", diary.diary_arr)
#next step I should add entry by input