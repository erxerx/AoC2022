def visible(xx, yy):
    r = True
    c = field[yy][xx]
    for lx in range(xx - 1, -1, -1):
        if field[yy][lx] >= c: r = False
    if r: return r
    r = True
    for lx in range(xx + 1, mx):
        if field[yy][lx] >= c: r = False
    if r: return r
    r = True
    for ly in range(yy - 1, -1, -1):
        if field[ly][xx] >= c: r = False
    if r: return r
    r = True
    for ly in range(yy + 1, my):
        if field[ly][xx] >= c: r = False
    return r


def scenic(xx, yy):
    cu = cd = cl = cr = 0
    c = field[yy][xx]
    for lx in range(xx - 1, -1, -1):
        cl += 1
        if field[yy][lx] >= c: break
    for lx in range(xx + 1, mx):
        cr += 1
        if field[yy][lx] >= c: break
    for ly in range(yy - 1, -1, -1):
        cu += 1
        if field[ly][xx] >= c: break
    for ly in range(yy + 1, my):
        cd += 1
        if field[ly][xx] >= c: break
    return cl * cr * cu * cd


with open('d08.ex', 'r') as f:
    d = f.readlines()
field = [x.replace('\n', '') for x in d]
mx = len(field[0])
my = len(field)
count = 2 * (mx + my) - 4  # subtract corners
for y in range(1, my - 1):
    for x in range(1, mx - 1):
        if visible(x, y):
            count += 1
print('Tallcount:', count)
biggest = 0
for y in range(1, my - 1):
    for x in range(1, mx - 1):
        if biggest < scenic(x, y):
            biggest = scenic(x, y)
print('Max scenic:', biggest)
