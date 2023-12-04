## find of power of an element


# function def 

def findPower(a , n):
    if n == 1:
        return a
    else:
        mid = n // 2
        b = findPower(a , mid)
        result = b*b
        if n % 2 == 0:
            return result
        else:
            return result * a


# Driver code

n = 10
a = 2
result = findPower(a,n)
print(result)


## Second method ----------------------------------------------------------------------------------------------------------------


# function def 

def findPowers( x , n ):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        n = -n
        x = 1/x
        return(x , n)
    else:
        mid  = n//2
        b = findPowers(x , mid)
        result = b*b
        
        if n  % 2 == 0:
            return result
        else:
            return result * x
    return result

# Driver code

x = 2
n = 10
result = findPowers( x , n )
print(result)