# write a program to greet user with "Good Day"
def greet(name):  # name1 value will automatically call by name 
    print("Good Day ",name)

def mySum(num1, num2):
    return num1 + num2

name1=input("Enter Your Name :")
greet(name1)
number1=int(input("Enter no1 :"))
number2=int(input("Enter no2 :"))
total = mySum(number1, number2)
print("SUM =",total)