def fibonacci(n):
    td = [0] * (n+1)
    td[0] = 0
    td[1] = 1
    for i in range(2,n+1):
        td[i] = td[i-1] + td[i-2]
    return td

l = fibonacci(100)
for i in range(len(l)):
    print(i, end=":")
    print(l[i], end=" ") 
