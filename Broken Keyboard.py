n = int(input())
for _ in range(n):
    s = input()
    i = 0
    arr = []
    while i < len(s):
        if i + 1< len(s) and s[i] ==s[i + 1]:
            i += 2
        else:
            arr.append(s[i])
            i += 1
    arr.sort()
    print("".join(arr))
