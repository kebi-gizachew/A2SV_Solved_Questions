# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        prev,inor=0,0
        def check(limit):
            nonlocal prev,inor
            if len(preorder)<=prev:
                return None
            if inorder[inor]==limit:
                inor+=1
                return None
            root=TreeNode(preorder[prev])
            prev+=1
            root.left=check(root.val)
            root.right=check(limit)
            return root
        return check(float("inf"))

        