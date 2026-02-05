class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_count=float(inf)
        arr=[]
        temp1=defaultdict(int)
        temp2=defaultdict(int)
        for i,j in enumerate(list1):
            temp1[j]=i
        for n,m in enumerate(list2):
            temp2[m]=n
        for k,l in temp1.items():
            if k in temp2 and min_count==l+temp2[k]:
                arr.append(k)
            if k in list2 and min_count>l+temp2[k]:
                if arr:
                    arr.pop()
                arr.append(k)
                min_count=l+temp2[k]
        return arr
            
            


        