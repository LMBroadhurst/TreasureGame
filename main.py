print("Welcome to the treasure map! You have 3 guesses to find the co-ordinates of the treasure :)")
print("Please check the readme file for instructions.")

row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]
row11 = ["_", "_", "_"]
row22 = ["_", "_", "_"]
row33 = ["_", "_", "_"]
map1 = [row1, row2, row3]
map2 = [row11, row22, row33]

print(f"{row1}\n{row2}\n{row3}")

import random

pc_choice_horiz = random.randint(0, 2)
pc_choice_vert = random.randint(0, 2)
map1[pc_choice_horiz][pc_choice_vert] = "x"

print("PC has hidden the treasure!\n")

user_lives = 0

while user_lives != 3:
    position = input("Where do you think the treasure is?\n")
    horizontal = int(position[0]) - 1
    vertical = int(position[1]) - 1
    if map1[horizontal][vertical] == "x":
        print("You have found the treasure!")
        user_lives = 3
    else:
        user_lives += 1
        print("Incorrect guess.")
        map2[horizontal][vertical] = "X"
        print(f"{row11}\n{row22}\n{row33}\n")
        if user_lives == 3:
            print("Sorry, you lost this time.")
            print("This is where the treasure was hiding!")
            print(f"{row1}\n{row2}\n{row3}")

print("\n\n\nThanks for trying my game :)")
