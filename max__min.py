## Find the max and min in the array


# function def

def findmaxmin(arr , i , j):

    # small problem
    # single element in array

    if i == j:
        max_val = arr[i]
        min_val = arr[j]

    # two element in array

    elif i == j-1:
        if arr[i] < arr [j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]

    # big problem

    else:
        mid = i + (j-i) // 2

        max_l , min_l = findmaxmin(arr , i , mid)
        max_r , min_r = findmaxmin(arr , mid+1 , j)

    # finding the final max_val

        if max_l < max_r:
            max_val = max_r
        else:
            max_val = max_l

    # finding the final min_val

        if min_l < min_r:
            min_val = min_l
        else:
            min_val = min_r


# Driver code

arr = [10 , 20 , 50 , 100 , 80 , 90]
i = 0
j = len(arr)-1

max_val , min_val = findmaxmin(arr , i , j)
print(max_val , min_val)