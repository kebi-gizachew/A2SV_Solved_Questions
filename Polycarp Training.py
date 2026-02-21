n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0
for i in arr:
    if i >= count + 1:
        count+= 1

print(count)
