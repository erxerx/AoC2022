with open('d12.in', 'r') as f:
    d = f.readlines()
field = [x.replace('\n', '') for x in d]
for i in range(len(field)):
    if 'S' in field[i]:
        sy = i
        sx = field[i].index('S')
    if 'E' in field[i]:
        ey = i
        ex = field[i].index('E')
mx = len(field[0])
my = len(field)
field[sy] = field[sy][:sx] + 'a' + field[sy][sx + 1:]
h = 'a'
steps = 0

ms = 0

def canstep(lx, ly, lh):
    global steps, ms
    if steps > ms:
        print(steps)
        ms = steps
    # print(lx + 1, ly + 1, lh)
    if lx < 0 or lx >= mx or ly < 0 or ly >= my: return False
    if lh == 'z' and field[ly][lx] == 'E':
        print('Finished at', steps)
        return True
    saved = field[ly][lx]
    if saved == '#' or ord(saved) > ord(lh) + 1:
        # print(saved)
        return False
    steps += 1
    field[ly] = field[ly][:lx] + '#' + field[ly][lx + 1:]
    if not canstep(lx, ly + 1, saved):
        if not canstep(lx + 1, ly, saved):
            if not canstep(lx - 1, ly, saved):
                if not canstep(lx, ly - 1, saved):
                    field[ly] = field[ly][:lx] + saved + field[ly][lx + 1:]
                    steps -= 1
                    return False
    print('Should not be here')
    return True


print(canstep(sx, sy, h))
while field[sy][sx] != 'E':
    if sx != 0:
        if canstep(sx - 1, sy, steps):
            print(steps)
            break




