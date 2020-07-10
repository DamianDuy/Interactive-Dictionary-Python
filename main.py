import json
from os import system, name

data = json.load(open("data.json"))

def clear():
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')    

def getDef(key):
    if key.lower() in data or key.upper() in data or key.title() in data:
        return data[key]
    else:
       
        return "Word does not appear to be in the dictionary."       
def addPosition():
    print("I am not doing anything yet.")

def delPosition():
    print("I am not doing anything yet.")

def show_menu():
    print("1. Look up the word.")
    print("2. Add a new word.")
    print("3. Add a new definition.")
    print("4. Delete the word.")
    print("5. Delete the definition.")
    print("6. Exit")

choice = "0"
while choice != "6":
    show_menu()
    choice = input()
    clear()
    if choice == "1":
        key = input("Enter the word: ")
        if isinstance(getDef(key), str):
            print(getDef(key))  
        else:
            for defin in getDef(key):
                print(defin)        
    if choice == "2" or choice == "3":
        addPosition()
    if choice == "4" or choice == "5":
        delPosition()
    if choice != "6":    
        input()            
        clear()