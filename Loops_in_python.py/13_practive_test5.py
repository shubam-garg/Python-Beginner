# Write a program to calculate the factorial of a given no using for loop
num=int(input("Enter the no:"))
n=1
for i in range(1,num+1):
    n=n*i
print("Fraction of ",num," is equal to ",n)