import json
from os import system, name
from difflib import get_close_matches

class Messages:
    @staticmethod
    def wordNotInDict():
        return "Word doesn't appear to be in a dictionary."
    @staticmethod
    def noOptInMenu():
        return "Not such option in the menu."
    @staticmethod
    def dictSaved():
        return "Dictionary saved."
    @staticmethod
    def dictNotSaved():
       return "You haven't saved your dictionary. If you are sure you want to quit type 'yes': "
    @staticmethod
    def insertWord(ifDelWarning = False):
        if not ifDelWarning:
            return "Insert the word: "
        else:
            return "Insert the word you want to delete (coresponding definitions will be deleted as well): "
    @staticmethod
    def insertDef(anotherDef = False):
        if not anotherDef:
           return "Insert the definition: "
        else:
            return "Do you wish to add another definition of the word? Type yes/no: "
    @staticmethod
    def showMenu():
       print("1. Look up the word.")
       print("2. Add a new word.")
       print("3. Add a new definition.")
       print("4. Delete the word.")
       print("5. Save a dictionary.")
       print("6. Exit")         
           

class Dictionary:
    def __init__(self):
        with open("data.json", "r") as rfile:
           self.data = json.load(rfile)

    def getDef(self, key):
       if key in self.data:
           return self.data[key]
       elif len(get_close_matches(key, self.data.keys(), cutoff=0.8)) == 1:
           return "Did you mean %s instead?" % get_close_matches(key, self.data.keys())[0]
       elif len(get_close_matches(key, self.data.keys(), cutoff=0.8)) == 2:
           return "Did you mean %s or %s instead?" % (get_close_matches(key, self.data.keys())[0], get_close_matches(key, self.data.keys())[1])
       elif len(get_close_matches(key, self.data.keys(), cutoff=0.8)) > 2:
           return "Did you mean %s, %s or %s instead?" % (get_close_matches(key, self.data.keys())[0], get_close_matches(key, self.data.keys())[1], get_close_matches(key, self.data.keys())[2])
       else:
           return Messages.wordNotInDict()

    def addPosition(self):
       print(Messages.insertWord(), end = '')
       key = input()
       print(Messages.insertDef(), end = '')
       value = input()
       self.data.setdefault(key, [])
       self.data[key].append(value)
       choice = "None"
       while choice.lower() != "no":
           print(Messages.insertDef(True), end = '')
           choice = input()
           if choice.lower() == "yes":
               print(Messages.insertDef(), end = '')
               value = input()
               self.data[key].append(value)
           elif choice.lower() != "no":
               print("Type yes/no.")

    def addDefin(self):
       key = input(Messages.insertWord())
       if key in self.data:
           print(Messages.insertDef(), end = '')
           value = input()
           self.data[key].append(value)
       else:
           print(Messages.wordNotInDict())  

    def delPosition(self):
       key = input(Messages.insertWord(True))
       if key in self.data:
           del self.data[key]
       else:
           print(Messages.wordNotInDict())

    def saveDict(self):
       with open("data.json", "w") as wfile:
           json.dump(self.data, wfile, sort_keys=True, indent=4)
       print(Messages.dictSaved())

def clear():
    if name == "posix":
        _ = system("clear")
    else:
        _ = system("cls")

def main():
    dictionary = Dictionary()
    choice = "0"
    ifSaved = False
    while choice != "6":
       i = 1
       Messages.showMenu()
       choice = input()
       clear()
       if choice == "1":
           key = input(Messages.insertWord())
           if isinstance(dictionary.getDef(key), str):
               print(dictionary.getDef(key))
           else:
               for defin in dictionary.getDef(key):
                   print("{}. {}".format(i, defin))
                   i += 1
       elif choice == "2":
            dictionary.addPosition()
       elif choice == "3":
           dictionary.addDefin()
       elif choice == "4":
           dictionary.delPosition()
       elif choice == "5":
           dictionary.saveDict()
           ifSaved = True
       elif choice != "6":
           print(Messages.noOptInMenu())
       if choice == "6" and not ifSaved:
           print(Messages.dictNotSaved(), end = '')
           quitMenu = input()
           if quitMenu.lower() != "yes":
               choice = 0
       if choice != "6":
           input()
           clear()
           
if __name__ == "__main__":
    main()