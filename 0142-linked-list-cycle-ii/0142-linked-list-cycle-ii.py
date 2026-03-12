# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        slow = head
        while fast and slow!=fast:
            fast = fast.next
            slow = slow.next
        return fast


        # if not head or not head.next:
        #     return None
        # fast = slow = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         break
        # else:
        #     return None
        # slow = head
        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next
        # return fast
        