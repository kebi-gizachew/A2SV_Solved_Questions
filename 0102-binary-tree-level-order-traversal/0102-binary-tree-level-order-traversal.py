# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            arr = []
            for t in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                arr.append(temp.val)
            res.append(arr)
        return res
            
                





















        # res = defaultdict(list)
        # def bfsDepth(root, depth):
        #     if not root:
        #         return
        #     res[depth].append(root.val)
        #     bfsDepth(root.left, depth+ 1)
        #     bfsDepth(root.right, depth+ 1)
        # result = []
        # bfsDepth(root , 0)
        # for i in range(len(res)):
        #     result.append(res[i]) 
        # return result

        # if not root:
        #     return []
        # queue = deque([root])
        # res = []
        # while queue:
        #     arr = []
        #     for t in range(len(queue)):
        #         temp = queue.popleft()
        #         arr.append(temp.val)
        #         if temp.left:
        #             queue.append(temp.left)
        #         if temp.right:
        #             queue.append(temp.right)
        #     res.append(arr)
        # return res















        # queue = deque([root])
        # res = [[root]]
        # while queue:
        #     arr = []
        #     for i in range(len(queue)):
        #         temp= queue.popleft()
        #         if temp:
        #             if temp.left:
        #                 arr.append(temp.left.val)
        #                 queue.append(temp.left.val)
        #             if temp.right:
        #                 arr.append(temp.right.val)
        #                 queue.append(temp.right.val)
        #     res.append(arr)
        # return res
                

            