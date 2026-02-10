n = int(input())
for _ in range(n):
  num = int(input())
  s = input()
  assets ={
    "aa" : 2,
    "aba" : 3,
    "aca" : 3,
    "acba" : 4,
    "abca" : 4,
    "abbaca" : 6,
    "accaba" : 6,
    "abbacca" : 7,
    "accabba" : 7
  }
  flag = True
  for i , j in assets.items():
    if i in s:
      print(j)
      flag = False
      break
  print(-1) if flag else None
