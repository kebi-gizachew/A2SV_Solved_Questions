class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n=list(map(str,nums))
        def order(x,y):
            if x+y<y+x:
                return 1
            if x+y>y+x:
                return -1
            else:
                return 0
        n.sort(key=cmp_to_key(order))
        k= ''.join(n)
        return "0" if k[0]=="0" else k


      
        
       