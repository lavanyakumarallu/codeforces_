for i in range(5):
    n = list(map(int, input("\n").strip().split()))[:5]
    for j in n:
        if j == 1:
            s = abs(2 - i) + abs(2 - n.index(j))
print(s)
