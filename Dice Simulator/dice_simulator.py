import random

x = "r"  # set variable r to roll dice loop

# loop and random method to continue rolling dice if user press "R" on keyboard
while x == "r":
    # used random method randint to generate integer random number in between 1 and 6
    face_number = random.randint(1, 6)
    # choose related face on the basis of random integer generated
    if face_number == 1:
        print('-----------')
        print('|         |')
        print('|    O    |')
        print('|         |')
        print('-----------')

    if face_number == 2:
        print('-----------')
        print('|         |')
        print('|  o   o  |')
        print('|         |')
        print('-----------')

    if face_number == 3:
        print('-----------')
        print('| O       |')
        print('|    O    |')
        print('|       O |')
        print('-----------')

    if face_number == 4:
        print('-----------')
        print('| O      O|')
        print('|         |')
        print('| O      O|')
        print('-----------')

    if face_number == 5:
        print('-----------')
        print('|O       O|')
        print('|    O    |')
        print('|O       O|')
        print('-----------')

    if face_number == 6:
        print('-----------')
        print('|O       O|')
        print('|O       O|')
        print('|O       O|')
        print('-----------')
    x = input("please press r to continue roll dice \n")
