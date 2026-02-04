class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x: x[0])
        for n,m in ranges:
            if n<=left<=m:
                if n<=right<=m:
                    return True
                else:
                    left=m+1
        return False

            
