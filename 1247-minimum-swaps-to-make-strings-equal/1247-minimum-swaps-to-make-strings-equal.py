class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        for i , j in zip(s1 , s2):
            if i + j == "xy":
                xy += 1
            elif i + j == "yx":
                yx += 1
        if (xy + yx) %2 != 0:
            return -1
        total = xy // 2
        total += yx //  2
        if xy % 2 != 0:
            total += 2
        return total
        