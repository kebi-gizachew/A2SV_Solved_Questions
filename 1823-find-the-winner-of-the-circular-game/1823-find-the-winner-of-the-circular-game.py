class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s = [i + 1 for i in range(n)]
        t = 0
        while len(s) > 1:
            t = (t + k - 1) % len(s)
            s.pop(t)
        return s[0]











        # l=[i for i in range(1,n+1)]
        # idx = 0
        # while len(l) > 1:
        #     idx = (idx + k - 1) % len(l)
        #     l.pop(idx)
        # return l[0]
        

        # arr=deque([i+1 for i in range(n)])
        # while len(arr)!=1:
        #     x=1
        #     num=arr.popleft()
        #     while x!=k:
        #         arr.append(num)
        #         x+=1
        #         num=arr.popleft()
        # return arr[0]

            


        