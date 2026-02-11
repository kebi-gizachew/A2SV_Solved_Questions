class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_t = Counter(t)
        count_s = Counter(s)
        r = count_t & count_s
        result = count_t - r
        finale = 0
        for i in result.values():
            finale += i
        return finale

        


        