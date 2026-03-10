"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        c = {}
        cur = head
        while cur:
            c[cur] = Node(cur.val)
            cur = cur.next
        m = head
        while m:
            i , j =m , c[m]
            j.next = c.get(i.next)
            j.random = c.get(i.random)
            m = i.next
        return c[head]
        