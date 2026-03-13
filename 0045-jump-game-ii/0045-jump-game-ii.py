class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        end = 0
        far = 0
        for i in range(len(nums) - 1):
            far = max(far , nums[i] + i)
            if i == end:
                end = far
                jump += 1
        return jump
