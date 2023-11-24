## count of number of way to reach upstairs :-



    


def helper(n):
    if n <= 1:
        return n
    return count(n-1) + count(n-2)


def count(s):
    return helper(s + 1)


# Driver code

n = 4
result = count(n)
print(result)
