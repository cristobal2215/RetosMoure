def Fibonacci(n):
    a=0
    b=1
    for i in range(50):
        c= a+b
        a=b
        b=c
    return b
for j in range(50):
    print (Fibonacci(j))
