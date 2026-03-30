# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def trial(num):
            if not num:
                return None
            temp= 0
            val = num[0]
            for i in range(len(num)):
                if num[i] >= val:
                    temp = i
                    val = num[i]
            root = TreeNode(val)
            root.left = trial(num[:temp])
            root.right = trial(num[temp +1:])
            return root
        return trial(nums)
        

        