def factorial(n):
    # Cover base cases
    if n==0 or n==1:
        return 1
    if n < 1:
        return -1
    
    # multiply all postiive integers below n 
    product = 1
    while(n > 1):
        product = product * n
        n = n-1
    
    return product

print(factorial(5))