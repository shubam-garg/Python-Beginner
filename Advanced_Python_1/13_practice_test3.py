# use comprehension function and print table of user enter no.
num=int(input("Enter any number to see the table of that number: "))
table=[num*i for i in range(1,11)]
print(table)