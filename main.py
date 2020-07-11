import json
from os import system, name
from difflib import get_close_matches

data = json.load(open("data.json"))

def clear():
    if name == "posix":
        _ = system("clear")
    else:
        _ = system("cls")    

def getDef(key):
    if key.lower() in data or key.upper() in data or key.title() in data:
        return data[key]
    elif len(get_close_matches(key, data.keys(), cutoff = 0.85)) == 1:
        return "Did you mean %s instead?" % get_close_matches(key, data.keys())[0]
    elif len(get_close_matches(key, data.keys(), cutoff = 0.85)) == 2:
        return "Did you mean %s or %s instead?" % (get_close_matches(key,data.keys())[0], get_close_matches(key,data.keys())[1])
    elif len(get_close_matches(key, data.keys(), cutoff = 0.85)) > 2:
        return "Did you mean %s, %s or %s instead?" % (get_close_matches(key,data.keys())[0], get_close_matches(key,data.keys())[1], get_close_matches(key,data.keys())[2])   
    else:
        return "Word does not appear to be in the dictionary."

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
    print("I am not doing anything yet.")

def delDefin():
    print("I am not doing anything yet.")

def showMenu():
    print("1. Look up the word.")
    print("2. Add a new word.")
    print("3. Add a new definition.")
    print("4. Delete the word.")
    print("5. Delete the definition.")
    print("6. Exit")

choice = "0"
while choice != "6":
    showMenu()
    choice = input()
    clear()
    if choice == "1":
        key = input("Enter the word: ")
        if isinstance(getDef(key), str):
            print(getDef(key))  
        else:
            for defin in getDef(key):
                print(defin)        
    if choice == "2":
        addPosition()
    if choice == "3":
        addDefin()    
    if choice == "4":
        delPosition()
    if choice == "5":
        delDefin()    
    if choice != "6":    
        input()            
        clear()