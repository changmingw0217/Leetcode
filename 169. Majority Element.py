class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}

        for num in nums:
            key = str(num)
            if key in count_dict:
                count_dict[key] += 1
            else:
                count_dict[key] = 1

        return max(count_dict, key=count_dict.get)

s = Solution()

s.majorityElement([3,2,3])