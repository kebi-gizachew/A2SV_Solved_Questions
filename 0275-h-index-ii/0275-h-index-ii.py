class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left , right = 0 , len(citations)
        ans = -1
        def checking_mid(mid):
            if mid < len(citations):
                return len(citations) - mid + 1 >= citations[mid]
            return False
        while right >= left:
            mid = left +(right - left)// 2
            if checking_mid(mid):
                ans = citations[mid]
                left = mid + 1
            else:
                right = mid - 1
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

        
        