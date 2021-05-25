try:
    a=int(input("enter the number: "))
    b=10/a
    print(b)

except ValueError as err:
    print("Value Error",err)

except ZeroDivisionError as err:
    print("Zero Division Error",err)

print("Thanks for visiting here")