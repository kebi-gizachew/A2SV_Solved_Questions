class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c = Counter()
        for i in bills:
            if i == 5:
                c[5] += 1
            if i == 10:
                if c[5] == 0:
                    return False
                c[5] -= 1
                c[10] += 1
            if i ==20:
                if c[5] == 0:
                    return False
                elif c[5] < 3 and c[10] == 0:
                    return False
                elif c[10] > 0 and c[5] > 0:
                    c[10] -= 1
                    c[5] -= 1
                elif c[5] >= 3:
                    c[5] -= 3
                else:
                    return False

        return True