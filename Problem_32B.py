s = input()
i = 0
x = str()
while i < len(s):
    if s[i] == '-' and s[i+1] == '.':
        x += '1'; i += 2
    elif s[i] == '-' and s[i+1] == '-':
        x += '2'; i += 2
    elif s[i] == '.':
        x += '0'; i += 1
print(x)
