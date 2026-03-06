# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        f1 = head
        f2 = head.next
        temp = f2
        while f2 and f2.next:
            f1.next = f2.next
            f1 = f1.next
            f2.next = f1.next
            f2 = f2.next
        f1.next = temp
        return head 




        
           







        # cur = head
        # while cur.next:
        #     temp = cur.next
        #     if temp.next:
        #         temp.next = temp.next.next
        #     cur.next= cur.next.next
        #     cur = cur.next


        