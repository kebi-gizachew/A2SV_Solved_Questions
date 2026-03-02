class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c = Counter()
        i = 0
        maxx = 0
        for r in range(len(fruits)):
            c[fruits[r]] += 1
            while len(c) > 2 and i < len(fruits):
                c[fruits[i]] -= 1
                if c[fruits[i]] == 0:
                    del c[fruits[i]]
                i += 1
            maxx = max(maxx , r-i+ 1)
        if maxx == 0 and len(c) == 2:
            return len(fruits)
        return maxx


        