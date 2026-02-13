t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()
    pos = x
    t1 = -1
    
    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            t1 = i + 1
            break
    if t1 == -1 or t1 > k:
        print(0)
        continue    
    pos = 0
    t2 = -1
    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1
        if pos == 0:
            t2 = i + 1
            break
    if t2 == -1:
        print(1)
        continue
    remaining = k - t1
    answer = 1 + remaining // t2
    
    print(answer)
