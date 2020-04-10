# first imported the json package to read dictionary json file.
import json

# loaded the json file in data variable using json package load method and opening a file using built-in function
data = json.load(open("dictionary.json"))


# user-defined function to refine the input and convert to the uppercase as dictionary file i'm using has uppercase
# notation as well as to prompt out message if word doesn't exist in file

def refine(find_def):
    find_def = find_def.upper()
    if find_def in data:
        return print(data[find_def])
    else:
        print("Word you're searching for doesn't exist in dictionary file")


find_def = input("what would you like to find out ?")
refine(find_def)
