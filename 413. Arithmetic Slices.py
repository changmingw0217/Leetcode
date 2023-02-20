class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0] * len(nums)
        result = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = 1 + dp[i-1]
                result += dp[i]
        return result


s = Solution()
s.numberOfArithmeticSlices([1,2,3,4])