# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        count = 0
        def coin_path(node):
            nonlocal count
            if not node:
                return 0
            left = coin_path(node.left)
            right = coin_path(node.right)
            count += abs(left) + abs(right)
            return node.val + left + right - 1
        coin_path(root)
        return count


        