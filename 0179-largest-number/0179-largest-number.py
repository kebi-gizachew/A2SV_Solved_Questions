class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = list(map(str, nums))
        def order(x , y):
            if x + y > y + x:
                return -1
            elif x+ y<y+x:
                return 1
            else:
                return 0
        s.sort(key = cmp_to_key(order))
        return "".join(s) if s[0] != "0" else "0"
        
        