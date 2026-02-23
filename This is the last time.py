n = int(input())
for _ in range(n):
    p , real = map(int, input().split())
    temp = []
    for t in range(p):
        l = list(map(int,input().split()))
        temp.append(l)
    temp.sort()
    for l , m, r in temp:
        if l<=real<=r:
            real = r
    print(real)




