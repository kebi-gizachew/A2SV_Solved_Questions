# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        m , n = list1 , list2
        dummy =ListNode(0)
        temp = dummy
        while m and n:
            if m.val > n.val:
                temp.next = n
                n = n.next
            else:
                temp.next = m
                m = m.next
            temp = temp.next
        if m:
            temp.next = m
        if n:
            temp.next = n
        return dummy.next
            
        

        