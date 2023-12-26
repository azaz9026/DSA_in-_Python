## Valid Palindrome -------------------------------------------------------------------------------------------------------------------------------


def validpalindrome(s):
    low = 0
    high = len(s) - 1

    while low < high:
        while low < high and not s[low].isalnum():
            low += 1
        while low < high and not s[high].isalnum():
            high -= 1

        if s[low].lower() != s[high].lower():
            return 'No'

        low += 1
        high -= 1

    return 'Yes'

s = "A man, a plan, a canal: Panama"
res = validpalindrome(s)
print(res)

# Ans -> Yes
