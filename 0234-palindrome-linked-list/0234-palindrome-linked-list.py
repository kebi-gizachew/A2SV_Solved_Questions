# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow , fast =head , head
        while fast and fast.next:
            fast= fast.next.next
            slow = slow.next  
        p =None
        while slow:
            temp = slow.next
            slow.next = p
            p = slow
            slow= temp
        while p:
            if head.val != p.val:
                return False
            head = head.next
            p = p.next
        return True


        