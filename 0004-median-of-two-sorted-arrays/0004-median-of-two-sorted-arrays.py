class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n.sort()
        v = len(n) // 2
        if len(n)% 2 == 0:
            return (n[v] +n[v-1]) / 2
        else:
            return n[v]


        
        