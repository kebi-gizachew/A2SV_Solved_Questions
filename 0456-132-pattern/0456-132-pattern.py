class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        res = float("-inf")
        stack = []
        for i in range(len(nums) -1 , -1 , -1):
            if res > nums[i]:
                return True
            while stack and stack[-1] < nums[i]:
                res = stack.pop()
            stack.append(nums[i])
        return False
            

        