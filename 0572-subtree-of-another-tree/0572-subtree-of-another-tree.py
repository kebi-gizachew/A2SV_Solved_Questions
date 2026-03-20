# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isSame(node , subNode):
            if not node and not subNode:
                return True
            if not node or not subNode:
                return False
            if node.val != subNode.val:
                return False
            return isSame(node.left , subNode.left) and isSame(node.right , subNode.right)
        return isSame(root,subRoot) or self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)

        