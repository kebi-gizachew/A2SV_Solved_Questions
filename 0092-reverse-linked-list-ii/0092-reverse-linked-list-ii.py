# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        start = None
        l , r = None , None
        for i in range(right):
            if i == left - 1:
                start = cur
            if i == left:
                l = cur
            if not cur:
                return head
            cur=cur.next
        r = cur
        prev = r.next if r else None
        r.next = None
        temp = l
        while temp:
            ctemp = temp.next
            temp.next = prev
            prev = temp
            temp = ctemp
        if start:
            start.next = prev
        return dummy.next
        



        