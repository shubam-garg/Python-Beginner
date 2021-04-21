# 4) find no is prime or not 
num=int(input("Enter the number:\t"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
        
if prime:
    print(num,"is a prime no")
else:
    print(num,"is not a prime no")