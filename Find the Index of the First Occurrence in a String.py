class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        r = len(needle)
        while r <= len(haystack):
            if needle == haystack[i:r]:
                return i
            r += 1
            i += 1
        return -1
        # arr=Counter(haystack[:len(needle)])
        # need=Counter(needle)
        # if arr==need:
        #     return 0
        # j=0
        # for i in range(len(needle),len(haystack)):
        #     arr[haystack[j]]-=1
        #     if arr[haystack[j]]==0:
        #         del arr[haystack[j]]
        #     arr[haystack[i]]+=1
        #     j+=1
        #     if arr==need:
        #         return j
        # return -1
