# file contain a word multiple times. you need to write program to replace that word by updating same file

with open("replace.txt") as f:
    text=f.read()

text = text.replace("I","______")

with open("replace.txt", "w") as f:
    f.write(text)