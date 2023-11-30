#maximum and minimum element in  an array

def max_min(arr , n):
    min_val = 0
    max_val = 0
    if arr[0] < arr[1]:
        max_val = arr[1]
        min_val = arr[0]
    else:
        max_val = arr[0]
        min_val = arr[1]
    
    for i in range( 2  , n):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr [i] < min_val:
            min_val = arr[i]
    
    return max_val , min_val




arr = [7, 1, 5, 3, 6, 10]
n = len(arr)

result = max_min(arr, n)
print(result)




