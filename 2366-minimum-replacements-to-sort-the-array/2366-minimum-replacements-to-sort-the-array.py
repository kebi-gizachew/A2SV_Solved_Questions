class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        front = nums[-1]
        count= 0
        for i in range(len(nums) -2 , -1 , -1):
            if front < nums[i]:
                temp = ceil(nums[i] / front)
                count += temp - 1
                front = nums[i] // temp
            else:
                front = nums[i]
        return count

        