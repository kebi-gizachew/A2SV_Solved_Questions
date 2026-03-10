# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        l = 1
        while tail.next:
            tail = tail.next
            l += 1
        k = k%l
        if k== 0:
            return head
        point = head
        for r in range(l - 1 - k):
            point = point.next
        new = point.next
        point.next = None
        tail.next = head
        return new