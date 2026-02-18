class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            lit = i
            for j in range(i + 1, len(heights)):
                if heights[j] > heights[lit]:
                    lit = j
            heights[i] , heights[lit] = heights[lit] ,  heights[i]
            names[i] ,  names[lit]= names[lit] , names[i]
        return names

        # d = defaultdict(str)
        # l =0
        # for i in heights:
        #     d[i] = names[l]
        #     l+=1
        # for i in range(len(heights)):
        #     for j in range(len(heights)-i - 1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j + 1] , heights[j]=heights[j], heights[j+1]
        # arr=[]
        # for k in heights:
        #     arr.append(d[k])
        # return arr
        
                
        
        # arr =[]
        # heights.sort(reverse=True)
        # for k in heights:
        #     arr.append(d[k])
        # return arr