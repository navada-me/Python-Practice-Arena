# first imported the json package to read dictionary json file.
import json
# imported get_close_matches package from difflib to get close matches from data i have in json file.
from difflib import get_close_matches


# loaded the json file in data variable using json package load method and opening a file using built-in function
data = json.load(open("dictionary.json"))


# user-defined function to refine the input and convert to the uppercase as dictionary file i'm using has uppercase
# notation as well as to prompt out message if word doesn't exist in file

def refine(find_def):
    find_def = find_def.upper()
    if find_def in data:
        return print(data[find_def])
    elif len(get_close_matches(find_def, data.keys())) > 0:
        print("Did you mean %s instead ?" % get_close_matches(find_def, data.keys())[0])
        decide = input("press y for Yes or n for No")
        if decide == "y":
            return print(data[get_close_matches(find_def, data.keys())[0]])
        elif decide == "n":
            return "you entered wrong input"
        else:
            return "Please enter either y or n"
    
    
    else:
        print("Word you're searching for doesn't exist in dictionary file")


find_def = input("what would you like to find out ?")
refine(find_def)
