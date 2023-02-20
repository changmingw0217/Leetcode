class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:

                if mid == left or nums[mid - 1] < target:
                    result.append(mid)

                right = mid - 1

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                if mid == right or nums[mid + 1] > target:
                    result.append(mid)
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if len(result) == 0:
            result = [-1, -1]

        return result

s = Solution()

print(s.searchRange([5,7,7,8,8,10], 8))