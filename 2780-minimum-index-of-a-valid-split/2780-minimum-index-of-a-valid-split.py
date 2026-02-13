class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        maxNum = 0
        c = Counter()
        flag = True
        k = 0
        for j , i in enumerate(nums):
            c[i] += 1
            maxNum = max(maxNum , c[i])
            if maxNum * 2 > j + 1 and j != 0:
                flag = False
                k = j + 1
                break
        if flag:
            return -1
        c1 = Counter(nums[k:])
        if max(c1.values()) * 2 > len(nums) - k:
            return k - 1
        else:
            return -1

        

        