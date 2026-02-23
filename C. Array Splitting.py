n , m = list(map(int, input().split()))
l = list(map(int,input().split()))

temp=[]
for i in range(len(l) - 1):
    diff = l[i + 1] - l[i]
    temp.append(diff)
temp.sort()

while m > 1 and len(temp) > 0:
    temp.pop()
    m -= 1
print(sum(temp))
