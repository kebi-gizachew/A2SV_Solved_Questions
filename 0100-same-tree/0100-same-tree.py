# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def treeIteration(t1 , t2):
            if t1 and not t2:return False
            if t2 and not t1:return False
            if not t1 and not t2:
                return True
            if t1.val != t2.val:
                return False
            return treeIteration(t1.left , t2.left) and treeIteration(t1.right , t2.right)
        return treeIteration(p , q)








        # queue1 = deque()
        # queue2 = deque()
        # while queue1 and queue2:
        #     t1 = queue1.popleft()
        #     t2 = queue2.popleft()
        #     if t1.val != t2.val:
        #         return False
        #     if t1.left:
        #         if not t2.left:
        #             return False
        #         queue1.append(t1.left)
        #     if t1.right:
        #         if not t2.right:
        #             return False
        #         queue1.append(t1.right)
        #     if t2.left:
        #         if not t1.left:
        #             return False
        #         queue2.append(t2.left)
        #     if t2.right:
        #         if not t1.right:
        #             return False
        #         queue2.append(t2.right)
        # return True






        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)
        