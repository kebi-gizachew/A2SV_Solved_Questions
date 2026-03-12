# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(float("inf"))
        dummy.next = head
        slow = dummy
        fast = dummy.next.next
        if not fast:
            return head 
        while fast:
            if fast.val != slow.next.val:
                slow = slow.next
                fast = fast.next
            else:
                while fast and fast.val == slow.next.val:
                    fast =fast.next
                if not fast:
                    slow.next = None
                    return dummy.next
                slow.next = fast
                fast = fast.next
        return dummy.next
            
            



                
        