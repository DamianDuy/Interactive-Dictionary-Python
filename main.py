import json
from os import system, name
from difflib import get_close_matches

with open("data.json", "r") as rfile:
    data = json.load(rfile)

def addPosition(key = "", value = ""):
    if value != "" and key not in data:
        data.setdefault(key, [])
        data[key].append(value)
        return "Word added successfully."
    elif key in data:
        return "Word already exists in the dictionary.\nTry adding a new definition."
    else:
        return "Cannot add the word without a definition."      

def getDef(key = ""):
    if key.lower() in data or key.upper() in data or key.title() in data:
        return data[key]
    elif len(get_close_matches(key, data.keys(), cutoff = 0.8)) == 1:
        return "Did you mean %s instead?" % get_close_matches(key, data.keys())[0]
    elif len(get_close_matches(key, data.keys(), cutoff = 0.8)) == 2:
        return "Did you mean %s or %s instead?" % (get_close_matches(key,data.keys())[0], get_close_matches(key,data.keys())[1])
    elif len(get_close_matches(key, data.keys(), cutoff = 0.8)) > 2:
        return "Did you mean %s, %s or %s instead?" % (get_close_matches(key,data.keys())[0], get_close_matches(key,data.keys())[1], get_close_matches(key,data.keys())[2])   
    else:
        return "Word does not appear to be in the dictionary."

def addDefin(key="", value=""):
    if value != "" and key in data:
       data[key].append(value)
       return "Definition added to the word '%s' successfully." %key
    elif key not in data:
        return "Word does not appear to be in the dictionary."
    else:
        return "Cannot add an empty definition."       

def delPosition(key = ""):
    if key in data:
        del data[key]
        return "Word deleted successfully."
    else:
        return "Word does not appear to be in the dictionary."
        
def saveDic():
    with open("data.json", "w") as wfile:
        json.dump(data, wfile, sort_keys = True, indent = 4)
    return ("Dictionary saved successfully.")    
'''
def addPosition():
    key = input("Insert the word: ")
    value = input("Insert definition: ")
    data.setdefault(key, [])
    data[key].append(value)
    choice = "None"
    while choice.lower() != "no":
        choice = input("Do you wish to add another definition of the word? Type yes/no: ")
        if choice.lower() == "yes":
            value = input("Insert definition: ")
            data[key].append(value)
        elif choice.lower() != "no":
            print("Type yes/no.")

def addDefin():
    key = input("Insert the word which definition you wish to add: ")
    if key in data:
        value = input("Insert definition: ")
        data[key].append(value)
    else:
        print("The word doesn't appear to be in a dictionary.")

def delPosition():
    key = input("Insert the word you want to delete (coresponding definitions will be deleted as well): ")
    if key in data:
        del data[key]
    else:
        print("The word doesn't appear to be in a dictionary.")

def saveDic():
    with open("data.json", "w") as wfile:
        json.dump(data, wfile, sort_keys = True, indent = 4)
    print("Dictionary saved.")    

def showMenu():
    print("1. Look up the word.")
    print("2. Add a new word.")
    print("3. Add a new definition.")
    print("4. Delete the word.")
    print("5. Save a dictionary.")
    print("6. Exit")

choice = "0"
ifSaved = False
while choice != "6":
    i = 1
    showMenu()
    choice = input()
    clear()
    if choice == "1":
        key = input("Enter the word: ")
        if isinstance(getDef(key), str):
            print(getDef(key))  
        else:
            for defin in getDef(key):
                print("{}. {}".format(i, defin))
                i += 1        
    elif choice == "2":
        addPosition()
    elif choice == "3":
        addDefin()    
    elif choice == "4":
        delPosition()
    elif choice == "5":
        saveDic()
        ifSaved = True
    elif choice != "6":
        print("No such option in the menu.")
    if choice == "6" and not ifSaved:
        quitMenu = input("You haven't saved your dictionary. If you are sure you want to quit type 'yes': ")
        if quitMenu.lower() != "yes":
            choice = 0                
    if choice != "6":    
        input()            
        clear()
'''