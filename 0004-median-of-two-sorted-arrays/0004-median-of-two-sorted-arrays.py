class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        arr= []
        idx = n // 2
        i , j = 0 , 0
        while len(arr) <= idx and i < len(nums1)and j < len(nums2):
            if nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j += 1
            else:
                arr.append(nums1[i])
                i += 1
        while len(arr) <= idx and j < len(nums2):
            arr.append(nums2[j])
            j += 1
        while len(arr) <=idx and i < len(nums1):
            arr.append(nums1[i])
            i += 1
        return ((arr[-2] + arr[-1]) / 2) if n % 2 == 0 else arr[-1]
        
            
















        # n = nums1 + nums2
        # def med(num):
        #     left = 0
        #     right = len(num) - 1
        #     mid = left +(right - left) // 2
        #     left = med(num[:mid])
        #     right = med(num[mid:])
        #     return order(left  , right)
        # def order(num1 , num2):
        #     arr= []
        #     if not num1:
        #         return num2
        #     if not num2:
        #         return num1
        #     while num1 and num2:
        #         if num1[0] > num2[0]:
        #             arr.append(num1[0])
        #             num1 = num1[1:]
        #         else:
        #             arr.append(num2[0])
        #             num2 = num2[1:]
        #     if num1:
        #         arr += num1
        #     if num2:
        #         arr += num2
        #     return arr
        # return med(n)
        
        
            











        # n = nums1 + nums2
        # n.sort()
        # v = len(n) // 2
        # if len(n)% 2 == 0:
        #     return (n[v] +n[v-1]) / 2
        # else:
        #     return n[v]


        
        