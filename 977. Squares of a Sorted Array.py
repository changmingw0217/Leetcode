class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = result_index = len(nums) - 1
        left = 0

        result = [0] * len(nums)
        while left <= right:

            left_r = nums[left] ** 2
            right_r = nums[right] ** 2

            if left_r ** 2 < right_r ** 2:
                result[result_index] = right_r
                result_index -= 1
                right -= 1
            else:
                result[result_index] = left_r
                result_index -= 1
                left += 1

        return result

s = Solution()

print(s.sortedSquares([-7,-3,2,3,11]))