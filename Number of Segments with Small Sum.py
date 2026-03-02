n , m = list(map(int , input().split()))
l = list(map(int, input().split()))
i = 0
temp = 0
op = 0
for r in range(len(l)):
    temp += l[r]
    while temp > m:
        temp -= l[i]
        i += 1
    op += r- i + 1
print(op)
 
