class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        c = Counter()
        for i in responses:
            temp = set(i)
            c.update(temp) 
        store = ""
        temp = 0
        for n, m in c.items():
            if m > temp or (m == temp and (store == "" or n < store)):
                store = n
                temp = m

        return store





# class Solution:
#     def findCommonResponse(self, responses: List[List[str]]) -> str:
#         c = Counter()
#         for i in responses:
#             r = list(set(i))
#             c += Counter(r)
#         print(c)
#         store = ""
#         temp = 0
#         for n , m in c.items():
#             if m > temp:
#                 store = n
#                 temp = m
#             elif m == temp:
#                 if store == "" or n < store:
#                     store = n
                # if n in store:
                #     store = n
                # elif store in n:
                #     continue
                # else:
                #     for i in range(min(len(n) , len(store))):
                #         if ord(store[i]) > ord(n[i]):
                #             store = n
                #             break
                #         elif ord(store[i]) < ord(n[i]):
                #             break     
        return store

