class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        maxx = [0] * k
        l1 , l2 = len(nums1) , len(nums2)
        def possible(a , b):
            stack = []
            drop = 0
            for n in a:
                while drop < len(a) - b and stack and stack[-1] < n:
                    stack.pop()
                    drop += 1
                stack.append(n)
            return stack[:b]
        def compare(a1 , a2):
            res = []
            while a1 or a2:
                if a1 > a2:
                    res.append(a1.pop(0))
                else:
                    res.append(a2.pop(0))
            return res

        for i in range(k + 1):
            if i <= l1 and k -i <= l2:
                arr1 = possible(nums1 , i)
                arr2 = possible(nums2 , k - i)
                temp = compare(arr1 , arr2)
                maxx = max(maxx , temp)
        return maxx


        