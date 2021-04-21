# Write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if n==1 or  n==0:
        return 1
    return n + sum(n-1)
    
''' 10+sum(9)
    10+9+sum(8)
    10+9+8+sum(7)
    10+9+8+7+sum(6)
    10+9+8+7+6+sum(5)
    10+9+8+7+6+5+sum(4)
    10+9+8+7+6+5+4+sum(3)
    10+9+8+7+6+5+4+3+sum(2)
    10+9+8+7+6+5+4+3+2+sum(1)
    10+9+8+7+6+5+4+3+2+1=55 '''

fr=sum(10)
print(fr)