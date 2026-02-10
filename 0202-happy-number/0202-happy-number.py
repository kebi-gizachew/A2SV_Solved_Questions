class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        k = n
        while k not in store:
            store.add(k)
            r = str(k)
            t = 0 
            for i in r:
                t += pow(int(i) , 2)
            k = t
        if k == 1:
            return True
        return False

        