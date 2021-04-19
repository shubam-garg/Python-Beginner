# Write a program to find the greatest of four numbers enter by user
w=int(input("Enter the no. 1 :"))
x=int(input("Enter the no. 2 :"))
y=int(input("Enter the no. 3 :"))
z=int(input("Enter the no. 4 :"))
if w>z:
    r=w
else:
    r=z

if x>y:
    s=x
else:
    s=y

if r>s:
    if w>z:
        print("no. 1 is greatest:",w)
    else :
        print("no. 4 is greatest:",z)
else :
    if x>y:
        print("no. 2 is greatest:",x)
    else :
        print("no. 3 is greatest:",y)