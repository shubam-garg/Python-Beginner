''' A spam comment is defined as a text containing following keywords.
    "make a lot of money","buy now","subscribe this","click this".
    Write a program to delete these spams. '''

text=input("Enter the text:\n")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this"):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("This is a spam")
else:
    print("This is not a spam")