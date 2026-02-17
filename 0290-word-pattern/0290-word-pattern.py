class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = defaultdict(str)
        i = 0
        arr = s.split()
        t = set()
        if len(arr)!=len(pattern):
            return False
        for k in pattern:
            if k not in d and arr[i] in t:
                return False
            if k not in d:
                d[k] = arr[i]
                t.add(arr[i])
                i+=1
            else:
                if arr[i] != d[k]:
                    return False
                i += 1
        return True
        