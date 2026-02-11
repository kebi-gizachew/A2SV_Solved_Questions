class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key = lambda x : abs(x))
        count = Counter(arr)
        for i in arr:
            if count[i] == 0:
                continue
            if count[i * 2] == 0:
                return False
            if i * 2 in count and count[i * 2] != 0:
                count[i] -= 1
                count[i * 2] -= 1
        return True
            
        