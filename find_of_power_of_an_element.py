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