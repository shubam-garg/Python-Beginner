''' Write a program to print a given star pattern:
        *
    *   *   *
*   *   *   *   * ''' 
''' n=4
for i in range(1,6,2):
    print(" "*n,"* " * i)
    n=n-2 '''

# or

n=3
for i in range(3):
    print(" " * (n-i-1) , end="") # end command donot allow to move to next line
    print("*" * ((2*i)+1) , end="")
    print(" " * (n-i-1))