class Solution:
    def romanToInt(self, s: str) -> int:
        sets = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }
        total = sets[s[0]]
        for i in range(1 , len(s)):
            if sets[s[i]] > sets[s[i - 1]]:
                total -= sets[s[i - 1]]
                total += sets[s[i - 1 : i + 1]]
            else:
                total += sets[s[i]]
        return total
            