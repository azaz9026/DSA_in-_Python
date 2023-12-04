## Sort Color -----------------------------------------------------------------------------

def sortColor(nums):

    p0 = 0
    curr = 0
    p2 = len(nums) - 1

    while curr <= p2:
        if nums[curr] == 0:
            nums[p0] , nums[curr] = nums[curr] , nums[p0]
            curr+=1
            p0+=1
        elif nums[curr] == 2:
            nums[p2] , nums[curr] = nums[curr] , nums[p2]
            p2-=1
        else:
            curr+=1
    return nums



nums = [ 2 , 0 , 2 , 1 , 1 , 0 ]
result = sortColor(nums)
print(result)

## Ans => [0, 0, 1, 1, 2, 2]

## The Time complexity => O(n)