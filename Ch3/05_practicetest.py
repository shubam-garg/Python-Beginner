#1
b=input("Enter Your Name\n")
print("Good Afternoon,\t"+b)

#2
letter = ''' Dear <!Name!>,
             You are  selected !
                         Date :<!Date!>'''
y=input("Please Enter Today's Date:\n")
letter=letter.replace("<!Name!>",b)
letter=letter.replace("<!Date!>",y)
print(letter)                           

#3
print(letter.find("  "))

#4
print(letter.replace("  "," "))

#5
st="Dear Shubi,\n\tThis Python course is nice.\nThanks!"
print(st)