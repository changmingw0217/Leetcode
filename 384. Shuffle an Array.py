import random
import copy

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.original_list = nums
        self.shuffled_list = []

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.original_list

    def shuffle(self):
        """
        :rtype: List[int]
        """
        l1 = copy.deepcopy(self.original_list)
        random.shuffle(l1)

        return l1


obj = Solution([1, 2, 3])

param_1 = obj.reset()

param_2 = obj.shuffle()


print(param_1)
print(param_2)