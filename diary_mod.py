class Diary:

    diary_arr = []
    #num_entries = 0

    def addEntry(self, date, entry, mood):
        entry_dict = {date:'Date', entry:'Entry', mood:'Mood'}
        self.diary_arr.append(entry_dict)
'''    def nonStop():
        num_entries = int(input("Enter the number of entries: "))
        while True:
            if num_entries == 0:
                diary.addEntry(date=input("Input the date"), entry=input("Input the text"), mood=input("Input the mood"))
                num_entries += 1
            break'''
        #asking entry and mood
        #call addEntry

diary = Diary() #create an instance of diary
diary.addEntry(date=input("Input the date: "), entry=input("Input the text: "), mood=input("Input the mood: "))
print("Test", diary.diary_arr)