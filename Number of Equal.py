n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i , j = 0 , 0
count = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        main = arr1[i]
        a1 , a2 = 0 , 0
        while i<len(arr1) and arr1[i] == main:
            a1 +=1
            i += 1
        while j <len(arr2) and arr2[j] ==main:
            a2+= 1
            j += 1
        count += a1 * a2
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        i += 1
print(count)
