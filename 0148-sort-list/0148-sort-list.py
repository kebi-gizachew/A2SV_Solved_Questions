# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1 , l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 =l1.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next
        
        def divide(head):
            if not head or not head.next:
                return head
            fast , slow = head.next, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            r = slow.next
            slow.next = None
            left = divide(head)
            right = divide(r)
            return merge(left , right)    

        
        return divide(head) 

       