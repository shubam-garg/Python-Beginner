# 4) Write a program to find whether a given username contains less than 10 characters or not

name=input("Enter the name :\n")
if(len(name)<10):
    print("length of username is less than 10 characters")
else:
    print("length of username is greater than or equal to 10 characters")


# 5) Write a program which finds out whether a given name is present in a list or not

Name=["Shubam","Shilpa","Sulekh","Raj"]
user=input("Enter the Name to check whether it exist in list or not:\n")
if(user in Name):
    print("It is present in the list")
else:
    print("It is not present in the list")