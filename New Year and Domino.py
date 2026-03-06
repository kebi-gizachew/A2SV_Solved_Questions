row , col = list(map(int , input().split()))
l = []
for r in range(row):
    l.append(input())
a1 = [[0] * (col + 1) for r in range(row + 1)]
a2=[[0] * (col+1) for i in range(row +1)]
for r in range(row):
    for c in range(col - 1):
        t = 0
        if l[r][c +1] == l[r][c] ==".":
            t += 1
        a1[r +1][c +1] = t + a1[r][c+1]+ a1[r +1][c] -a1[r][c]
 
for r in range(row - 1):
    for c in range(col):
        t = 0
        if l[r + 1][c] == l[r][c] ==".":
            t += 1
        a2[r +1][c +1] = t + a2[r][c+1]+ a2[r +1][c] -a2[r][c]
q = int(input())
 
for _ in range(q):
    r1 , c1 , r2, c2 = list(map(int , input().split()))
    x = a1[r2][c2-1] - a1[r1 - 1][c2-1] - a1[r2][c1 - 1] + a1[r1 - 1][c1 - 1]
    y = a2[r2-1][c2] - a2[r1 - 1][c2] - a2[r2-1][c1 - 1] + a2[r1 - 1][c1 - 1]
    print(x + y)
 
