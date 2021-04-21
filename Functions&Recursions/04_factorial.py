def factorial_iteration(n):
    product=1
    for i in range(n): 
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n==1 or  n==0:
        return 1
    return n * factorial_recursive(n-1)

f=factorial_iteration(5)
g=factorial_recursive(5)
print(f)
print(g)