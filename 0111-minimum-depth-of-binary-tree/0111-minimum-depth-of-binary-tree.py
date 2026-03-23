# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def count(root):
            if not root.left and not root.right:
                return 1
            if root.left and root.right:
                return 1 + min(count(root.left) , count(root.right))
            if not root.right:
                return 1 + count(root.left)
            if not root.left:
                return 1 + count(root.right)
        return count(root)
            
        