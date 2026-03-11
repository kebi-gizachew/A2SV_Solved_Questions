class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        finale = {}
        for i in range(len(nums2) - 1 , -1 , -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                finale[nums2[i]] = stack[-1]
            else:
                finale[nums2[i]] = -1
            stack.append(nums2[i])
        f = []
        for t in nums1:
            f.append(finale.get(t))
        return f




        # arr=[0]*(max(nums2)+1)
        # stack=[]
        # for i in range(len(nums2)-1,-1,-1):
        #     while stack and nums2[stack[-1]]<nums2[i]:
        #         stack.pop()
        #     if stack:
        #         arr[nums2[i]]=stack[-1]
        #     else:
        #         arr[nums2[i]]=-1
        #     stack.append(i)
        # count=[]
        # for k in nums1:
        #     if arr[k]!=-1:
        #         count.append(nums2[arr[k]])
        #     else:
        #         count.append(-1)
        # return count

            
                

        