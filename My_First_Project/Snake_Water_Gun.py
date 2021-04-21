# Creating a game of snake, water and gun in pyhton

import random 
# random package contain randint function which gives value randomly with in given parameters

def game(comp, player):
    if comp == player:
        print("Tie")
    if comp == "s":
        if player == "w": 
            print("You Loose the Match")
        elif player == "g":
            print("You Won the Match")
    elif comp == "w":
        if player == "s":
            print("You Won the Match")
        elif player == "g":
            print("You Loose the Match")
        
    elif comp == "g":
        if player == "s":
            print("You Loose the Match")
        elif player == "w":
            print("You Won the Match")
        
    else:
        print("There is some problem")

player = input("Turn of Player : Snake(s) Water(w) or Gun(g)? :")
if player != 's' and player != 'w' and player != 'g':
    print("Your Input is invalid") 
else:
    r = random.randint(1, 3)
    if r==1:
       comp="s"
    elif r==2:
       comp="w"
    else:
        comp="g"
        print("Turn of Computer : Snake(s) Water(w) or Gun(g)? :"+ comp)
    game(comp, player)