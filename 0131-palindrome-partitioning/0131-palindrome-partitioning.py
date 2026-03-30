class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        def trial(letters):
            if not letters:
                for t in path:
                    i , j = 0 ,len(t) -1
                    while j > i:
                        if t[j] != t[i]:
                            return
                        j -=1 
                        i += 1
                res.append(path[:])
                return
            for i in range(len(letters)):
                path.append(letters[:i +1])
                trial(letters[i +1:])
                path.pop()
        trial(s)
        return res