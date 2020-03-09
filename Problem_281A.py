s = input()
l = list(s)
if s[0].islower():
    l[0] = s[0].upper()
print("".join(l))
