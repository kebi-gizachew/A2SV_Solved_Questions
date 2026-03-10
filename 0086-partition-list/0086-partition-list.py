# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = ListNode(0)
        curr = odd
        even = ListNode(0)
        even.next= head
        temp = even
        while temp.next:
            if temp.next.val < x:
                curr.next = temp.next
                curr = curr.next
                temp.next = temp.next.next
            else:
                temp = temp.next
        even = even.next
        curr.next= even
        return odd.next
        