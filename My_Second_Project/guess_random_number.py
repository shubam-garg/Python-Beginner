from math import e
import random

randomNum=random.randint(1,100)
print(randomNum)
enterNum=None
while(enterNum!=randomNum):
    enterNum=int(input("Enter your guess: "))
    if enterNum==randomNum:
        print("Your guess is right")
    elif enterNum<randomNum:
        print("Your guess is lower")
    else:
        print("Your guess is bigger")

