# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        stack = []
        cur = head
        while cur:
            while stack and stack[-1].val< cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        r = ListNode(0)
        res = r
        for i in stack:
            res.next = i
            res= res.next
        return r.next

        