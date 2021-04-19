# Write a program to print multiplication table of n using for loop in reversed order

num=int(input("Enter the no. to print table:"))
for i in range(10,0,-1):
    print(f"{num} X {i} = {num*i}") # it is known as f string
