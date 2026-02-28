n = int(input())
for _ in range(n):
    num = int(input())
    arr = list(map(int, input().split()))
    t = False
    if len(arr) > 1 and arr[1] - arr[0] >0:
        t = True
    finale=[]
    finale.append(str(arr[0]))
    for r in range(1 , len(arr)):
        if t and arr[r] - arr[r - 1] < 0:
            finale.append(str(arr[r - 1]))
            t = not t
        if not t and arr[r] - arr[r-1]>0:
            finale.append(str(arr[r - 1]))
            t = not t
    if finale[-1] !=arr[-1]:
        finale.append(str(arr[-1]))
    print(len(finale))
    print(" ".join(finale))
        
