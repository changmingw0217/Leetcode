class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        result_index = 0
        for i in range(1, len(intervals)):
            item = intervals[i]
            r_item = result[result_index]
            if r_item[1] < item[0]:
                result.append(item)
                result_index += 1
            else:
                result[result_index][1] = max(result[result_index][1], item[1])
        return result

s = Solution()
print(s.merge([[1,4],[4,5]]))