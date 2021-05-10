''' The game() function in a program lets a user play a game and returns the score as an integer.
    you need to read a file "hi-score.txt" which is either blank or contains the previous high score.
    You need to write a program to update high score whenever game() breakes the high score'''
def game():
    return 12

score=game()
print("You have scored:",score)
with open("hi-score.txt", "r") as f:
    highscorestr=f.read()

if highscorestr=='': 
    with open("hi-score.txt", "w") as f:
        f.write(str(score))
    with open("hi-score.txt", "r") as f:
        print("New highest score is:",f.read())
elif int(highscorestr)<score:
    with open("hi-score.txt", "w") as f:
        f.write(str(score))
    with open("hi-score.txt", "r") as f:
        print("New highest score is:",f.read())
else:
    with open("hi-score.txt","r") as f:
        print("Your highest score is:",f.read())