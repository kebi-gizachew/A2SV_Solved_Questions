class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] *len(nums)
        suf = [1]*len(nums)
        finale= []
        for i in range(1 , len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
            suf[len(nums)-i - 1] = suf[len(nums) -i] * nums[len(nums) -i]       
        for t in range(len(nums)):
            finale.append(pre[t] * suf[t])
        return finale
        




        