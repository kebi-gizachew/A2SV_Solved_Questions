class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        op = 0
        r = 0
        temp = min(len(g) , len(s))
        for t in g:
            while r< len(s) and t> s[r]:
                r+= 1
            if r == len(s):
                return op
            op += 1
            r += 1
        return op
        


        