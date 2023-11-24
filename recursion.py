## the recursion function Call itself directly or indirectly 

## factorial 

def findfactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * findfactorial(n-1)


n = 5
result = findfactorial(n)
print('The factorial is that' , result)


## using the iterative approcah

def findfactorial1(n):
    res = 1
    if n == 0 or n == 1:
        return 1 
    else:
        for i in range(0 , n+1):
            res = res * i 
        return res

n = 1
ans = findfactorial1(n)
print('The Answer is That' , ans)

