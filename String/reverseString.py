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

## Function Calling

Str = "Azaz khan"
result = reverseString(Str)
print(result)

## Ans => nahk zazA
## Time complexit => O(n)


## another Method-----------------------------------------------------------------------------------------------------------------------

def reverseString(s):
    # Convert the string to a list
    str_list = list(s)

    low = 0
    high = len(str_list) - 1

    while low < high:
        temp = str_list[low]
        str_list[low] = str_list[high]
        str_list[high] = temp
        low += 1
        high -= 1

    # Join the list back into a string
    reversed_str = ''.join(str_list)

    return reversed_str

Str = "Azaz khan"
result = reverseString(Str)
print(result)

## Ans => nahk zazA
## Time complexit => O(n)

## another Method-----------------------------------------------------------------------------------------------------------------------



def reverse_whole_string(s):
    return s[::-1]

# Example
my_string = "Hello, World!"
reversed_string = reverse_whole_string(my_string)
print("Reversed string:", reversed_string)

## Ans => nahk zazA



