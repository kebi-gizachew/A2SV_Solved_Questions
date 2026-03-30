class Solution:
    def splitString(self, s: str) -> bool:
        path = []
        def trial(nums):
            if not nums:
                if len(path) >=2:
                    for i in range(len(path) -1 , 0, -1):
                        if int(path[i]) + 1 != int(path[i -1]):
                            return False
                    return True
                return False

            for i in range(len(nums)):
                path.append(int(nums[:i + 1]))
                if trial(nums[i + 1:]):
                    return True
                path.pop()
            return False                
        return trial(s)
        



