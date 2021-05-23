class boss:
    def __init__(self,num): # front and back use of __ means a dunder method
        self.num=num

    def __add__(self,num2):     # this already define in python
        return self.num+num2.num

    def __mul__(self,num2):     # this already define in python, num2 is overloaded
        return self.num*num2.num

    def __truediv__(self,num2):
        return self.num/num2.num

n=boss(90)
n1=boss(10)
sum=n+n1
multiply=n*n1
divide=n/n1
print(sum)
print(multiply)
print(divide)