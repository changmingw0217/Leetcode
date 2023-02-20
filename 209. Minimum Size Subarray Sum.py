import sys
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = j = sum_result = subLen = 0
        result = sys.maxsize

        while j < len(nums):
            sum_result += nums[j]

            while sum_result >= target:
                subLen = j - i + 1
                result = min(result, subLen)
                sum_result -= nums[i]
                i += 1

            j += 1

        if result == sys.maxsize:
            return 0

        return result

s = Solution()
print(s.minSubArrayLen(4, [1, 1, 1]))