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