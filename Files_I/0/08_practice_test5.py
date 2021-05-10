# repeat a program 4 for a list of such words to be censored

words = ["Dog","Donkey","Monkey"]

with open("replace1.txt") as f:
    text=f.read()

for word in words:
    text = text.replace(word,"$%#@$%$##&")
    with open("replace1.txt", "w") as f:
        f.write(text)  