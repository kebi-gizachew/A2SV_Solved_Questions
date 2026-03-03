class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        op = 0
        for i in range(1 , len(nums)):
            nums[i] +=nums[i - 1]
        print(nums)
        for t in range(len(nums) - 1):
            if (nums[len(nums) - 1] - nums[t] - nums[t])%2 ==0:
                op +=1
                print(op)
        return op if op !=0 else 0
        