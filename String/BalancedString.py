## Split a String in Balanced String -----------------------------------------------------------------------------------------------------------


def BalancedString(s):
    r = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'R':  # Use square brackets for indexing, and use single quotes for character literals
            r += 1
        else:
            r -= 1
        
        if r == 0:
            count += 1 

    return count

s = "RLRRLLRLRL"
res = BalancedString(s)
print(res)

# Ans => 4
# Time Complexity = O(n)