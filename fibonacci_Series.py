## fibonacci series using recurision :-

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10  
for i in range(n):
    print(fibonacci(i))  


## Ans be that 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34


    