# Write a program to print multiple table of given no using for loop

num=int(input("Enter the no. to print table:"))
for i in range(1,11):
    # print(num," X ",i," = ",num*i)
    
    # or

    print(f"{num} X {i} = {num*i}") # it is known as f string

#using while loop
l=1
while l<=10:
    print(num," X ",l," = ",num*l)
    l=l+1