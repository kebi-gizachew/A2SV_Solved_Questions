# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def finale(root, total):
            nonlocal count
            if not root:
                return None
            def isSum(node, summ):
                nonlocal count
                if not node:
                    return None
                summ += node.val
                if summ == targetSum:
                    count += 1
                isSum(node.right , summ)
                isSum(node.left , summ)
            isSum(root , 0)
            finale(root.left , 0)
            finale(root.right , 0)
            return count
        return finale(root, targetSum) if root else count
            

        