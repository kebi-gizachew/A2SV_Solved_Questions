# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre, post = 0, 0 
        def prePost(value):
            nonlocal pre, post
            root = TreeNode(value)
            pre += 1
            if value != postorder[post] and pre  <len(preorder):
                root.left = prePost(preorder[pre])
            if value != postorder[post] and pre < len(preorder):
                root.right = prePost(preorder[pre])
            post += 1
            return root
        return prePost(preorder[0])

        