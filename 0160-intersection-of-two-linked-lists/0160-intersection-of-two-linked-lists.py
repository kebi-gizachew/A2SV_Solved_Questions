# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headA.next:
            return None
        if not headB or not headB.next:
            return None
        s1 , s2 = headA, headB
        op = 0
        while s1!=s2:
            if not s1:
                s1 = headB
                s2=s2.next
            if not s2:
                s2 = headA
                s1 = s1.next
            else:
                s1 = s1.next
                s2 = s2.next
        return s1
        