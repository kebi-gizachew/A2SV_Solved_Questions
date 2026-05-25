class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for i in nums:
            b = bisect.bisect_left(sub , i)
            if len(sub) <= b:
                sub.append(i)
            else:
                sub[b] = i
        return len(sub)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna