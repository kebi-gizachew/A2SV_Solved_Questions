class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left , right = 0 , len(citations) - 1
        ans = 0
        while right >= left:
            mid = left +(right - left) // 2
            if len(citations) - mid <= citations[mid]:
                ans = len(citations) - mid
                right = mid - 1
            else:
                left = mid +1
        return ans













        # left = 0
        # right = len(citations)
        # ans= -1
        # while right >= left:
        #     mid = left+(right-left)//2
        #     if citations[mid - 1] <= mid:
        #         ans = citations[mid - 1]
        #         left=  mid+1
        #     else:
        #         right = mid - 1
        # return ans

        
        