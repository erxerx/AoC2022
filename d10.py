with open('d10.ex', 'r') as f:
    d = f.readlines()
data = [x.replace('\n', '').split(' ') for x in d]
x = cycle = runtime = 1
pc = ss = 0
line = ''
lines = []
while pc < len(data):
    if abs((runtime % 40 - 1) - x) < 2:
        line += '#'
    else:
        line += '.'
    if not cycle:
        op = data[pc]
        if op[0] == 'noop':
            cycle = 1
        if op[0] == 'addx':
            cycle = 2
            x += int(op[1])
        pc += 1
    cycle -= 1
    runtime += 1
    if runtime % 40 == 20:
        ss += (runtime * x)
    if runtime % 40 == 0:
        print(line)
        lines.append(line)
        line = ''
print(ss)
