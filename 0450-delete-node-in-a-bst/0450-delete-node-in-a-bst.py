# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteRoot(root, target):
            if not root:
                return None
            if target > root.val:
                root.right = deleteRoot(root.right , target)
            elif target < root.val:
                root.left = deleteRoot(root.left, target)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right= deleteRoot(root.right , temp.val)
            return root
        return deleteRoot(root , key)



        