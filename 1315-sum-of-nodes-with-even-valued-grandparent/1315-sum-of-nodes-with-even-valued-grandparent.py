# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def evenSum(node, parent , grandParent):
            nonlocal summ
            if not node:
                return None
            if grandParent % 2 == 0:
                summ +=node.val
            evenSum(node.left , node.val , parent)
            evenSum(node.right , node.val , parent)
        evenSum(root, -1, -1)
        return summ

        