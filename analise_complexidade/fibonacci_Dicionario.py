def fibonacci(n):
    if n==0 or n==1:
        return n
    if n not in td.keys():
       td[n] = fibonacci(n-1) + fibonacci(n-2) 
    
    return td[n]

td = {}
print(fibonacci(10))