## count of number of way to reach upstairs :-



    


def helper(n):
    if n <= 1:
        return n
    return helper(n-1) + helper(n-2)


def count(s):
    return helper(s + 1)


# Driver code

n = 4
result = count(n)
print(result)






