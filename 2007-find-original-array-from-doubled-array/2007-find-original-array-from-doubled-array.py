class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if len(changed) % 2 != 0:
        #     return []
        # changed.sort()
        # count = Counter(changed)
        # ans = []
        # for x in changed:
        #     if count[x] == 0:
        #         continue

        #     if count[2 * x] == 0:
        #         return []

        #     ans.append(x)
        #     count[x] -= 1
        #     count[2 * x] -= 1

        # return ans
       

            
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        assets = Counter(changed)
        org = []
        for k in changed:
            if assets[k] == 0:
                continue
            if assets[k * 2] == 0:
                return []
            assets[k] -= 1
            assets[k * 2] -= 1
            org.append(k)
        return org 

        