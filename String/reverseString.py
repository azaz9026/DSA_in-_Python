## Reverse String --------------------------------------------------------------------------------------------------------------------------------


def reverseString(Str):
    Str = list(Str)
    low = 0
    high = len(Str)-1

    while low < high:
        temp = Str[low]
        Str[low] = Str[high]
        Str[high] = temp
        low += 1
        high -= 1

    return ''.join(Str)




Str = "Azaz khan"
result = reverseString(Str)
print(result)