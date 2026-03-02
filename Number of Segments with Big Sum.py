n , m = list(map(int , input().split()))
l = list(map(int , input().split()))
summ = l[0]
op =0
k = 0
for i in range(len(l)):
    while summ < m and k + 1 < len(l):
        k += 1
        summ += l[k]
    if k + 1 >=len(l) and summ < m:
        break
    op += len(l) -k
    summ -= l[i]
print(op)
