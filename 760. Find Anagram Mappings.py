class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums1:
            if num in nums2:

                result.append(nums2.index(num))
        return result


s = Solution()

r = s.anagramMappings([12,28,46,32,50], [50,12,32,46,28])

print(r)