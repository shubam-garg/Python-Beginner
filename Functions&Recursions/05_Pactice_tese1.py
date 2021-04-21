# write a program using function to find three greatest of three numbers
def maxno(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(num1,"num1 is greatest no.")
        else:
            print(num3,"num3 is greatest no.")
    else:
        if num2>num3:
            print(num2,"num2 is greatest no.")
        else:
            print(num3,"num3 is greatest no.")

maxno(77,274,166)

    
        