x = int(input())
c = 0
while x != 0:
  d = x%10
  x = x // 10
  c += 1
  if d != 7 and d != 4:
    c -= 1 
if c == 4 or c== 7:
  print('YES')
else:
  print('NO')
