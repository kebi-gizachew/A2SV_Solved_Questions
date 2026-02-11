class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        count = Counter(nums)
        for i in nums:
            if count[i] == 0:
                continue
            m = 1
            while m < k:
                if i + m not in count or count[i + m] == 0:
                    return False
                count[i + m] -= 1
                m += 1
            count[i] -= 1
        return True


        