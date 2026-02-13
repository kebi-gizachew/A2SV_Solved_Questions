temp=[]
for i in range(5):
    arr=list(map(int,input().split()))
    if 1 in arr:
        print(abs(2-i)+abs(2-arr.index(1)))
        break
    temp.append(arr)
