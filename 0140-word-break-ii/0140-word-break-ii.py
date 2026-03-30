class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sets = set(wordDict)
        path = []
        res = []
        def trial(letter):
            if not letter:
                res.append(" ".join(path[:]))
                return

            for i in range(len(letter)):
                if letter[:i + 1] not in sets:
                    continue
                path.append(letter[:i +1])
                trial(letter[i + 1:])
                path.pop()
        trial(s)
        return res

        