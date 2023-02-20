# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        li = []

        while fast and fast.next:
            li.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        for i in range(len(li) - 1, -1, -1):
            if slow.val != li[i]:
                return False
            slow = slow.next

        return True
