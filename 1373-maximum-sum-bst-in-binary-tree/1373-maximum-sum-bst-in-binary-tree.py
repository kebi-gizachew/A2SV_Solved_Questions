# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxx = 0
        def trial(root):
            nonlocal maxx
            if not root:
                return (True , float("-inf") , float("inf") , 0)
            lTrue , lmax , lmin , lsumm = trial(root.left)
            rTrue , rmax , rmin , rsumm = trial(root.right)
            if lTrue and rTrue and lmax < root.val < rmin:
                maxx = max(maxx , root.val + lsumm + rsumm)
                s = root.val + lsumm + rsumm
                return (True , max(rmax , root.val) , min(lmin , root.val) , s)
            return (False , 0 , 0 , 0)
        trial(root)
        return maxx








        # maxx = 0
        # def trial(root):
        #     nonlocal maxx
        #     if not root:
        #         return 0
        #     left = trial(root.left)
        #     right = trial(root.right)
        #     if right == 0:
        #         right = root.val + 1
        #     if (left != -1 and left < root.val and right != -1 and right > root.val) :
        #         maxx = max(maxx , root.val +left + right)
        #         return left + right + root.val
        #     return -1
        # trial(root)
        # return maxx
            
            









        # def summ(root, s):
        #     if not root:
        #         return
        #     s += root.val
        #     summ(root.left , s)
        #     summ(root.right, s)
        #     return s

        # def trial(root):
        #     if not root.left and not root.right:
        #         return False
        #     if not root.left:
        #         if root.right.val > root.val:
        #             return True
        #         return False
        #     if not root.right:
        #         if root.left.val < root.val:
        #             return True
        #         return False
        # flag = trial(root)
        


        

        