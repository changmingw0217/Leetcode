def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    lastZero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastZero] = nums[i]
            lastZero += 1

    for i in range(lastZero, len(nums)):
        nums[i] = 0


moveZeroes([0,1,0])
