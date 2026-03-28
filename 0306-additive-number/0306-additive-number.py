class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        path = []
        if len(num) <3:
            return False
        def trial(nums):
            if not nums:
                if len(path) < 3:
                    return False
                for i in range(len(path) - 2):
                    if int(path[i]) + int(path[i + 1]) != int(path[i + 2]):
                        return False
                return True
                        
            for i in range(len(nums)):
                part = nums[:i + 1]
                if part.startswith("0") and len(part) > 1:
                    break
                path.append(nums[:i + 1])
                if trial(nums[i+ 1:]):
                    return True
                path.pop()
            return False
        return trial(num)
        
            



        