n = int(input())
m = list(map(int,input().split()))
m.sort()
if n%2==0:
    x = n//2
    print(m[x-1])
    exit()
print(m[n//2])
