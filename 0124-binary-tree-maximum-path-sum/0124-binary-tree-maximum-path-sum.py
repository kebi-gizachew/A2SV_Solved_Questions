# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = float("-inf")
        def trial(root):
            nonlocal maxx
            if not root:
                return float("-inf")
            left= trial(root.left)
            right = trial(root.right)
            if left == float("-inf"):
                left = 0
            if right == float("-inf"):
                right = 0
            maxx = max(maxx , root.val + left + right , root.val + left , root.val+ right , root.val)
            return max(root.val + left , root.val + right , root.val)
        trial(root)
        return maxx



        