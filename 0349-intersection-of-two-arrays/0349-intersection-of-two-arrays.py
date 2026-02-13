class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # arr=set()
        # for i in nums1:
        #     if i in nums2:
        #         arr.add(i)
        # return list(arr)
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1 & s2)
            

        