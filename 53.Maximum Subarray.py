def maxSubarray(nums):
    curr_max = nums[0]
    max_so_far = nums[0]

    for i in range(1,len(nums)):
        curr_max = max(curr_max, curr_max + nums[i])
        max_so_far = max(curr_max, max_so_far)

    return max_so_far