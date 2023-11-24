print(""'''
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
'''"")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice = []
choice.append( input('You\'re at a cross road.\nWhere do you want to go? Type "left" or "right"\n').lower())
if choice[0] == "right":
    print("You fell into a hole. Game Over.")
elif choice[0] == "left":
    choice.append(input('You\'ve come to a lake.\nThere is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower())
    if choice[1] == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif choice[1] == "wait":
        choice.append(input('You arrive at the island unharmed.\nThere is a house with 3 doors.One red, one yellow and one '
                        'blue.\nWhich colour do you choose ? ').lower())
        match choice[2]:
            case "blue":
                print("Eaten by beasts.Game Over.")
            case "red":
                print("Burned by fire. Game Over")
            case "yellow":
                print("You win")
            case _:
                print("You loose")

##
