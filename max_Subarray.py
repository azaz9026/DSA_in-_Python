## find the Max Product SubArray

def maxSubArray(arr , n):
    if len(arr) == 0:
        return 0
    
    res = arr[0]

    for i in  range(0 , n):
        accs = 1
        for j in range(i , n):
            accs *= arr[j]
            res = max(res , accs)
    return res




arr = [2,3,-2,4]
n = len(arr)

result = maxSubArray(arr, n)
print(result)