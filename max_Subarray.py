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


def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result

# Example
nums = [-1, 0, 1, 2, -1, -4]
output = three_sum(nums)
print(output)  # Output: [[-1, -1, 2], [-1, 0, 1]]
