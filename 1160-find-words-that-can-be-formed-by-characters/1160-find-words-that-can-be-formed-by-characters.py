class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        a=Counter(chars)
        t=0
        for i in words:
            if Counter(i)<=a:
                t+=len(i)
        return t
        