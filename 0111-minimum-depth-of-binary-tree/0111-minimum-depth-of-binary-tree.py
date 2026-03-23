# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def count(root):
            if not root:
                return 0
            if not root.left:
                return 1 + count(root.right)
            if not root.right:
                return 1 + count(root.left)
            return 1 + min(count(root.right) , count(root.left))
        return count(root)
            
        