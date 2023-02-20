class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        slowIndex = 0
        print(nums)

        for i in range(len(nums)):

            if nums[i] != val:

                nums[slowIndex] = nums[i]

                slowIndex += 1

        return slowIndex


s = Solution()
print(s.removeElement([0,1,2,3,3,0,4,2], 2))