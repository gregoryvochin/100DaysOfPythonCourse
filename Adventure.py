print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")

if road == "right":
    print("You turn right and are immediately struck by a charging buffalo. Game over.")
    
else:
    print("You turn left and come to a lake. There is an island in the middle of it.")
    swim = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")

    if swim == "swim":
        print("You decide to swim across but are sucked into a whirlpool. Game over.")

    else:
        print("You decide to wait for a boat and make it across the water safely.")
        print("There is a mansion in the middle of the island with three doors.")
        doors = input("Which do you enter? Red, Yellow, or Blue?")

        if doors == "red":
            print("The door doesn't budge. You are then sprayed with gasoline and lit on fire. Game over.")

        elif doors == "blue":
            print("You rush to enter and fall into a pit of snakes. They kill you. Game over.")

        else:
            print("You found the treasure! Game over. You win!")
