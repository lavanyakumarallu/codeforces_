y = int(input())
while True:
    l = list(str(y+1))
    if (l[0] != l[1]) and (l[0] != l[2]) and (l[0] != l[3]) and (l[1] != l[2]) and (l[1] != l[3]) and (l[2] != l[3]):
        print(int("".join(l)))
        break
    y = int("".join(l))
