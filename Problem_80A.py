n, m = map(int, input().strip().split())
flag = True
while flag == True:
  n += 1
  for i in range(2, n):
    if n % i == 0:
      break
  else:
    flag = False
if n == m:
  print('YES')
else:
  print('NO')
