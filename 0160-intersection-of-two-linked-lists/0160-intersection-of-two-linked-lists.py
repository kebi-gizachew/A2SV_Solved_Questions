# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1,l2=headA,headB
        if not l1 or not l2:
            return None
        while l1!=l2:
            if not l1:
                l1=headB
                l2=l2.next
                continue
            if not l2:
                l2=headA
                l1=l1.next
                continue
            l1=l1.next
            l2=l2.next
        return l1
        