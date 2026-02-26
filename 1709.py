n = int(input())
for _ in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    op = 0
    finale = []
    for i in range(m):
        if a[i] > b[i]:
            a[i] , b[i] = b[i], a[i]
            finale.append((3,i+1))
            op += 1

    for k in range(m):
        t = a[k]
        i = k - 1
        while i >= 0 and a[i] > t:
            a[i+1] =a[i]
            finale.append((1 , i + 1))
            op += 1
            i -= 1
        a[i + 1] = t
    for c in range(m):
        t = b[c]
        i = c - 1
        while i >= 0 and b[i] > t:
            b[i+1] =b[i]
            finale.append((2 , i + 1))
            op += 1
            i -= 1
        b[i + 1] = t
    print(op)
    for x in finale:
        print(*x)
    


        
        
