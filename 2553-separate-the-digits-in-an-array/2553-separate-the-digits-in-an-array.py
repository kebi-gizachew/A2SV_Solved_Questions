class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in nums:
            r=str(i)
            for k in r:
                arr.append(int(k))
        return arr


        