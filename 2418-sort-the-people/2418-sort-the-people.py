class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = defaultdict(str)
        l =0
        for i in heights:
            d[i] = names[l]
            l+=1
        arr =[]
        heights.sort(reverse=True)
        for k in heights:
            arr.append(d[k])
        return arr
        # for i in range(len(heights)):
        #     for j in range(len(heights)-i - 1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j + 1] , heights[j]=heights[j], heights[j+1]
        # arr=[]
        # for k in heights:
        #     arr.append(d[k])
        # return arr
        
                
        