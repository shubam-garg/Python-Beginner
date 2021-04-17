''' 1)Write a program to create a dictionary in hindi words 
    with values as english trnaslation.provide option to user
    to look it up. '''
dic = {
        "Pankha":"Fan",
        "Kursi":"Chair",
        "Cha":"Tea"
        }
print("options available with you are ",dic.keys())
a=input("enter the value\n:")
# print("the meaning of the word you enter is :",dic[a])   # through error if key not present
print("the meaning of the word you enter is :",dic.get(a))# will not through error if key not present

