import json
from os import system, name
from difflib import get_close_matches

class Messages:
    @staticmethod
    def wordNotInDict():
        return "Word doesn't appear to be in a dictionary."
    @staticmethod    
    def wordWithoutDef():
        return "Cannot add the word without a definition."
    @staticmethod
    def wordAddSucc():
        return "Word added successfully."
    @staticmethod
    def wordAlrExists():
        return "Word already exists in the dictionary.\nTry adding a new definition."
    @staticmethod
    def emptyDef():
        return "Cannot add an empty definition."
    @staticmethod
    def wordDelSucc():
        return "Word deleted successfully."
    @staticmethod
    def dictSaveSucc():
        return "Dictionary saved successfully." 

class Dictionary:
    def __init__(self):
       with open("data.json", "r") as rfile:
           self.data = json.load(rfile)

    def addPosition(self, key = "", value = ""):
       if value != "" and key not in self.data:
           self.data.setdefault(key, [])
           self.data[key].append(value)
           return Messages.wordAddSucc()
       elif key in self.data:
           return Messages.wordAlrExists()
       else:
           return Messages.wordWithoutDef()     

    def getDef(self, key = ""):
       if key in self.data:
           return self.data[key]
       elif len(get_close_matches(key, self.data.keys(), cutoff = 0.8)) == 1:
           return "Did you mean %s instead?" % get_close_matches(key, self.data.keys())[0]
       elif len(get_close_matches(key, self.data.keys(), cutoff = 0.8)) == 2:
           return "Did you mean %s or %s instead?" % (get_close_matches(key, self.data.keys())[0], get_close_matches(key, self.data.keys())[1])
       elif len(get_close_matches(key, self.data.keys(), cutoff = 0.8)) > 2:
           return "Did you mean %s, %s or %s instead?" % (get_close_matches(key,self.data.keys())[0], get_close_matches(key, self.data.keys())[1], get_close_matches(key, self.data.keys())[2])   
       else:
           return Messages.wordNotInDict()

    def addDefin(self, key="", value=""):
       if value != "" and key in self.data:
          self.data[key].append(value)
          return "Definition added to the word '%s' successfully." %key
       elif key not in self.data:
          return Messages.wordNotInDict()
       else:
          return Messages.emptyDef()      

    def delPosition(self, key = ""):
       if key in self.data:
           del self.data[key]
           return Messages.wordDelSucc()
       else:
           return Messages.wordNotInDict()
        
    def saveDict(self):
       with open("data.json", "w") as wfile:
           json.dump(self.data, wfile, sort_keys = True, indent = 4)
       return Messages.dictSaveSucc()