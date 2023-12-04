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


# Second method --------------------------------------------------------------------------


def maxSubArray(nums):

    if len(nums) == 0:
        return 0
        
    max_so = nums[0]
    min_so = nums[0]
    result = max_so

    for i in range( 1 , len(nums)):
        curr = nums[i]
        temp = max(curr , max(curr*max_so , curr*min_so))
        min_so = min(curr , min(curr*max_so , curr*min_so))

        max_so = temp

        result = max( max_so , result )
    
    return result

nums = [2,3,-2,4]

result = maxSubArray(nums)
print(result)