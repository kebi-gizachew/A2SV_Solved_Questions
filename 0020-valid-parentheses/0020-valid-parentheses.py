class Solution:
    def isValid(self, s: str) -> bool:
        c = {")":"(","}":"{","]":"["}
        p =[]
        for i in s:
            if i not in c:
                p.append(i)
            else:
                if p:
                    t = p.pop()
                    if t != c[i]:
                        return False
                
        if p:
            return False
        return True


        