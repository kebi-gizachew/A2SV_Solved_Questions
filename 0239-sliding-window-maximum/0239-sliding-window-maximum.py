class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        finale = []
        for i in range(k):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        finale.append(stack[0])
        for r in range(k , len(nums)):
            if stack and nums[r - k] == stack[0]:
                stack.popleft()
            while stack and stack[-1] < nums[r]:
                stack.pop()
            stack.append(nums[r])
            finale.append(stack[0])
        return finale

        