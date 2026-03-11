# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while True:
            fast = start
            for i in range(k):
                if not fast:
                    return dummy.next
                fast = fast.next
            if not fast:
                return dummy.next
            prev = fast.next
            fast.next = None
            cur= start.next
            while cur:
                t = cur.next
                cur.next = prev
                prev = cur
                cur = t
            y = start
            start = start.next
            y.next = prev
        return dummy.next






        
        