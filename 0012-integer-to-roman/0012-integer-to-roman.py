class Solution:
    def intToRoman(self, num: int) -> str:
        comp={
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I",
        }
        r=num
        finale=""
        for i,j in comp.items():
            temp=0
            if r>=i:
                temp=r//i
                r%=i
                finale+=j*temp
        return finale
