t = int(input())
for _ in range(t):
    n = int(input())
    l1 = list(map(int ,input().split()))
    m = int(input())
    l2 = list(map(int , input().split()))
    maxx1 = 0
    maxx2 = 0
    summ1 = 0
    summ2 = 0
    for i in range(len(l1)):
        summ1 += l1[i]
        maxx1 = max(maxx1 , summ1)
    for t in range(len(l2)):
        summ2 += l2[t]
        maxx2 = max(maxx2 , summ2)
    print(maxx1 + maxx2)
 
