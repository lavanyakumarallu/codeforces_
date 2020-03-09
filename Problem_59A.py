s = input()[:100]
c_u, c_l = 0, 0
for i in range(len(s)):
    if s[i].isupper():
        c_u += 1
    else:
        c_l += 1
if c_u > c_l:
    print(s.upper())
elif c_u == c_l:
    print(s.lower())
else:
    print(s.lower())
