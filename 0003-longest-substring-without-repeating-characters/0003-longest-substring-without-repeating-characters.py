class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charStore = defaultdict(int)
        maxx = 0
        for t in range(len(s)):
            if s[t] in charStore:
                tempChar = charStore[s[t]]
                if start <= tempChar:
                    start = tempChar + 1
            maxx = max(maxx , t - start + 1)
            charStore[s[t]] = t
        return maxx

















        # arr=Counter()
        # l = 0
        # op = 0 
        # for i in range(len(s)):
        #     if s[i] in arr:
        #         op = max(op , i - l)
        #         while s[l] != s[i]:
        #             del arr[s[l]]
        #             l+= 1
        #         if l!=i:
        #             l+=1
        #     else:
        #         arr[s[i]] += 1
        # op = max(op , len(arr))
        # return op


            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna