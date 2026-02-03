class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=strs[0]
        for i in strs[1::]:
            while i.find(k)!=0:
                k=k[:-1]
                if not k:
                    return ""
        return k
            
            
        
