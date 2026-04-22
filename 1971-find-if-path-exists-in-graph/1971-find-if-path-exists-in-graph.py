class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = defaultdict(list)
        visited = set()
        for x , y in edges:
            path[x].append(y)
            path[y].append(x)
        def cycle(i):
            nonlocal destination
            if i == destination:
                return True
            visited.add(i)
            for t in path[i]:
                if t in visited:
                    continue
                if cycle(t):
                    return True
            return False
        return cycle(source)