class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n=[]
        for i in range(len(arr),1,-1):
            m=arr.index(i)
            if m!=i-1:
                if m!=0:
                    arr[:m+1]=arr[:m+1][::-1]
                    n.append(m+1)
                arr[:i]=arr[:i][::-1]
                n.append(i)
        return n

        