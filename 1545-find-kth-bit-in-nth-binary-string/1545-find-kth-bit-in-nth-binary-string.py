class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def drive_back(num):
            if num == 1:
                return "0"
            temp = drive_back(num - 1)
            r = []
            for i in range(len(temp) - 1 , -1 , -1):
                r.append(str(int(temp[i]) ^ 1))
            fin = "".join(r)
            return temp +"1" + fin
        other = drive_back(n)
        return other[k - 1]


            


        