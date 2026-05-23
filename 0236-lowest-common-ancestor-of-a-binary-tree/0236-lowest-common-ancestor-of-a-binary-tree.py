# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = None
        def dfs(node):
            nonlocal temp
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                temp = node
                return True
            if (left or right) and (node == p or node == q):
                temp = node
                return True
            if node == p or node == q:
                return True
            if left or right:
                return True
            return False
        dfs(root)
        return temp

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna