class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=Counter()
        l = 0
        op = 0 
        for i in range(len(s)):
            if s[i] in arr:
                op = max(op , i - l)
                while s[l] != s[i]:
                    del arr[s[l]]
                    l+= 1
                if l!=i:
                    l+=1
            else:
                arr[s[i]] += 1
        op = max(op , len(arr))
        return op


            


        