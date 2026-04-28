# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue= deque([root])
        while queue:
            temp = queue.popleft()
            if temp:
                if temp.left and temp.left.val != temp.val:
                    return False
                if temp.right and temp.right.val != temp.val:
                    return False
                queue.append(temp.left)
                queue.append(temp.right)
        return True
        








        # if not root:
        #     return True
        # def cycle(root,val):
        #     if not root:
        #         return True
        #     if root.val != val:
        #         return False
        #     return cycle(root.left, val) and cycle(root.right, val)
        # return cycle(root, root.val)

            






        # d = deque([root])
        # vis = set([root])
        # while queue:
        #     temp = quesu()
        # # check = True
        # # def sameValued(root):
        # #     if not root:
        # #         return -1
        # #     left = sameValued(root.left)
        # #     right = sameValued(root.right)
        # #     check &= (left == right == root.val)
        # #     return root.val
        # # sameValued(root)
        # # return check
        