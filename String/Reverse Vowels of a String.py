## Reverse Vowels of a String --------------------------------------------------------------------------------------------------------------------


def reverseVowels(s):
    s = list(s)
    low = 0
    high = len(s)-1

    Vowels = {'a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U'}

    while low < high:

        if s[low] in Vowels and s[high] in Vowels:
            s[low] , s[high] = s[high] , s[low]
            low += 1
            high -= 1

        elif s[low] in Vowels:
            high -= 1

        else:
            low += 1
    
    return "".join(s)




s = "hello"
res = reverseVowels(s)
print(res)



##  comments to explain each part of your code:-------------------------------------------------------------------------------------------------



def reverseVowels(s):
    # Convert the input string to a list of characters
    s = list(s)
    # Initialize two pointers, low at the beginning and high at the end
    low, high = 0, len(s) - 1

    # Set of vowels to check against
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Continue swapping vowels until low pointer is greater than or equal to high pointer
    while low < high:
        # If both characters at low and high pointers are vowels, swap them
        if s[low] in vowels and s[high] in vowels:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        # If only the character at low pointer is a vowel, move high pointer left
        elif s[low] in vowels:
            high -= 1
        # If only the character at high pointer is a vowel, move low pointer right
        else:
            low += 1
    
    # Convert the list back to a string and return the result
    return "".join(s)

# Example usage
s = "hello"
res = reverseVowels(s)
print(res)
