class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: defaultdict(int))
        op = 0
        for i in range(len(nums)):
            g = gcd(k , i)
            if nums[i] in d:
                g = gcd(k, i)
                for t in d[nums[i]]:
                    if (g * t) % k == 0:
                        op+=d[nums[i]][t]
            d[nums[i]][g] += 1
        return op

                




        # d = defaultdict(list)
        # op =0
        # if not nums:
        #     return 0
        # for i , j in enumerate(nums):
        #     d[j].append(i)
        # for n , m in d.items():
        #     if len(m) > 1:
        #         for j in range(len(m)):
        #             for y in range(j+1,len(m)):
        #                 if m[j] * m[y]% k ==0:
        #                     op += 1
        # return op





        
        