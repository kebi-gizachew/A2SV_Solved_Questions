class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        maxx = float("inf")
        def trial(arr, i , j):
            nonlocal maxx
            if i == len(cookies):
                maxx = min(maxx , max(arr))
                return
            if j >= k:
                return
            arr[j] += cookies[i]
            trial(arr , i + 1 , 0)
            arr[j] -= cookies[i]
            if arr[j] != 0:
                trial(arr , i , j + 1)
        trial([0 for i in range(k)] , 0 , 0)
        return maxx










        # maxx = float("inf")
        # def trial(arr , cookie):
        #     nonlocal maxx
        #     if cookie >= len(cookies):
        #         maxx = min(maxx , max(arr))
        #         return

        #     for i in range(k):
        #         arr[i] += cookies[cookie]
        #         trial(arr , cookie + 1)
        #         arr[i] -= cookies[cookie]
        # trial([0 for i in range(k)] , 0) 
        # return maxx








        # maxx = float("inf")
        # def trial(child , i , j):
        #     nonlocal maxx
        #     if i == len(cookies):
        #         maxx = min(maxx, max(child))
        #         return
        #     if j >= k:
        #         return
        #     child[j] += cookies[i]
        #     trial(child , i + 1 , 0)
        #     child[j] -= cookies[i]
        #     if child[j] !=0:
        #         trial(child , i , j + 1)
        # trial([0 for i in range(k)] , 0 , 0)
        # return maxx





        # # def trial(child , i):
        # #     nonlocal maxx
        # #     if i == len(cookies):
        # #         maxx = min(maxx , max(child))
        # #         return
        # #     for n in range(k):
        # #         child[n] += cookies[i]
        # #         trial(child , i + 1)
        # #         child[n] -= cookies[i]
          
        # trial([0 for i in range(k)] , 0)
        # return maxx
        



        






       