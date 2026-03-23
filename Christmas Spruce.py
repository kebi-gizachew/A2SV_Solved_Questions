n = int(input())
tree = [[] for i in range(n +1)]
sets = set()
for i in range(2 , n + 1):
    x = int(input())
    tree[x].append(i)
    sets.add(x)
for s in sets:
    count = 0
    for i in tree[s]:
        if not tree[i]:
            count += 1
    if count < 3:
        print("No")
        exit()
    
print("Yes")
 
 
