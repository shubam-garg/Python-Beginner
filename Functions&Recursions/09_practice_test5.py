''' Write a python function to print first n lines of the following pattern:
    * * *
    * *
    *     '''
n=3
for i in range(n):
    print(" * " * (n-i))


'''  Write a python function to converts inches to cms '''
def cms(inches):
    return inches * 2.54

i=cms(5)
print(i)