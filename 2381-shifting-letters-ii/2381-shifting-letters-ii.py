class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for i , j ,k in shifts:
            if k ==1:
                arr[i] += 1
                arr[j + 1] -= 1
            else:
                arr[i] -= 1
                arr[j + 1] += 1
        for t in range(1 , len(arr)):
            arr[t] += arr[t - 1] 
        arr.pop()
        finale = []
        for a in range(len(arr)):
            t = arr[a]
            f = chr((ord(s[a]) - ord("a") + t)%26 + ord("a"))
            finale.append(f)
        return "".join(finale)

        
        