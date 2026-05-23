class Solution:
    def longestPalindrome(self, s: str) -> str:
        res= ""
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j]

        for i in range(len(s)):
            odd = expand(i , i)
            even = expand(i , i +1)
            if len(res) < len(odd):
                res = odd
            if len(res) < len(even):
                res = even
        return res        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna