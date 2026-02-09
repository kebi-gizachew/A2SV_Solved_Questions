class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp=defaultdict(list)
        for k in strs:
            r=[0]*26
            for i in k:
                r[ord(i)-ord("a")]+=1
            temp[tuple(r)].append(k)
        return list(temp.values())
        

        
