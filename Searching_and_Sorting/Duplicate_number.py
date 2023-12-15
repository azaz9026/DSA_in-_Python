## Duplicate Number in the array -----------------------------------------------------------------------------------------------------------------------------------


def find_duplicate_number(arr):
    # Initialize a set to keep track of seen numbers
    seen = set()

    # Iterate through the array
    for num in arr:
        # Check if the number is already in the set
        if num in seen:
            return num  # Return the number as a duplicate
        else:
            seen.add(num)  # Add the number to the set

    return None  # Return None if no duplicate is found

# Example usage:
arr = [1, 2, 3, 4, 5, 2, 6, 7]
result = find_duplicate_number(arr)
print(result)



## another method ------------------------------------------------------------------------------------------------------------------------------------------------



def find_duplicate_number(arr):
    duplicate = -1

    # Iterate through the array
    for i in range(len(arr)):
        curr = abs(arr[i])
        
        # Check if the current element is negative
        if arr[curr] < 0:
            duplicate = curr
            break
        else:
            # Mark the current element as visited by making it negative
            arr[curr] *= -1

    return duplicate

# Example usage:
arr = [1, 2, 3, 4, 5, 2, 6, 7]
result = find_duplicate_number(arr)
print(result)
