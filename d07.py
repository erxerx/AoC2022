with open('d07.in', 'r') as f:
    d1 = f.read().split('\n$ ')
data = [x.split('\n') for x in d1]
pwd = ['/']
sizes = {}
recsizes = {}
for c in data:
    if c[0][:2] == 'cd':
        if c[0] == 'cd /':
            pwd = ['/']
        elif c[0] == 'cd ..':
            pwd.pop()
        else:
            pwd.append(c[0][3:])
    elif c[0][:2] == 'ls':
        for i in c[1:]:
            if i[:3] == 'dir':
                continue
            if '/'.join(pwd) not in sizes:
                sizes['/'.join(pwd)] = 0
            sizes['/'.join(pwd)] += int(i.split(' ')[0])
            cwd = pwd[:]
            while cwd:
                if '/'.join(cwd) not in recsizes:
                    recsizes['/'.join(cwd)] = 0
                recsizes['/'.join(cwd)] += int(i.split(' ')[0])
                cwd.pop()
            # print('/'.join(pwd), sizes['/'.join(pwd)])
s = 0
for d in recsizes:
    if recsizes[d] <= 100000:  # remove for part2
        s += recsizes[d]
print('Total:', s)
srt = dict(sorted(recsizes.items(), key=lambda item: - item[1]))
missing = 30000000 - 70000000 + recsizes['/']
print('Missing:', missing)
t1 = t2 = 0
for ss in srt:
    t2 = t1
    t1 = srt[ss]
    if srt[ss] < missing:
        break
print('Del:', t2)
