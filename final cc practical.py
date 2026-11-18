def maxSubArray(nums):
    curr = maxi = nums[0]

    for n in nums[1:]:
        curr = max(n, curr + n)
        maxi = max(maxi, curr)

    return maxi


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))