# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        res = []
        visited = set()
        def dfs(node):
            if not node:
                return
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
            dfs(node.right)
            dfs(node.left)
        def dfs2(val, target):
            if val in visited:
                return
            visited.add(val)
            if target == 0:
                return res.append(val.val)
            for i in graph[val]:
                dfs2(i, target - 1)
        dfs(root)
        dfs2(target, k)
        return res
            



        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna