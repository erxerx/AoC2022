def points(cc):
    if cc > 'Z':
        return ord(cc) - 96
    else:
        return ord(cc) - 38


with open('d03.ex', 'r') as f:
    d = f.readlines()
data = [x.replace('\n', '') for x in d]
s1 = s2 = 0
b1 = b2 = ''
for i, b in enumerate(data):
    x = b[0:int(len(b) / 2)]
    y = b[int(len(b) / 2):]
    for c in x:
        if c in y:
            s1 += points(c)
            break
    if i % 3 == 2:
        for c in b:
            if c in b1 and c in b2:
                s2 += points(c)
                break
    b2 = b1
    b1 = b
print('Total1:', s1)
print('Total2:', s2)
