# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        for i in range(1,len(lists)):
            lists[i]=self.merging(lists[i-1],lists[i])
        return lists[-1]

    def merging(self,l1,l2):
        d=ListNode()
        t=d
        while l1 and l2:
            if l1.val<l2.val:
                t.next=l1
                l1=l1.next
                t=t.next
            else:
                t.next=l2
                l2=l2.next
                t=t.next
        if l1:
            t.next=l1
        if l2:
            t.next=l2
        return d.next
        