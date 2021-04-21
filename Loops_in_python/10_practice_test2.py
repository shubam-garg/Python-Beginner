'''  Write a program to greet all the names stored in a list l1 and which starts with s. '''

l1=["Shubam","Raj","Shilpa","Faizan"]
for name in l1:
    if name.startswith("S"):
        print("Dear ",name)