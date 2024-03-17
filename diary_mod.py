diary_Dict = {}
class Diary(object):
    def __init__(self, entry):
        self.entry = entry
        entry = input("What are you thinking about? ")
        diary_Dict[:] = {"Entry":entry}
    def menu():
        while True:
            print("Press 1 to add entry")
            choose = input("Enter a choose: ")
            if choose == 1:
                Diary(object)
            else:
                break
    if __name__ == "__main__":
       menu()