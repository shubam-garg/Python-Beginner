''' Write a program to print following pattern
    *   *   *
    *       *
    *   *   * '''
n=int(input("Enter the no:"))
for i in range(0,n):
    if(i==0 or i==(n-1)):
        print(" * " * n)
    elif(i!=n):
        print(" * " * (n-(n-1)) , end="")
        print("   " * (n-2) , end="")
        print(" * " * (n-(n-1)))