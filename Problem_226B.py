n, t = map(int, input().strip().split())
s = input()[:n]
s = list(s)
for i in range(t):
    j = 0
    while j < n-1: 
        if s[j] == 'B' and s[j+1] == 'G':
            s[j], s[j+1] = s[j+1], s[j]
            j = j + 2   
        else:
            j += 1
print("".join(s))
