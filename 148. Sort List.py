# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)


    def getMid(self, head):
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        mid, slow.next = slow.next, None
        return mid

    def merge(self, left, right):
        tail = dummy = ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next

