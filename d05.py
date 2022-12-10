with open('d05.ex', 'r') as f:
    content = f.read()
n = 3
d1 = content.split('\n\n')
c1 = d1[0].split('\n')
c1.reverse()
orders = [x.split(' ') for x in d1[1].split('\n')]
stacks1 = [[] for x in range(n)]
for x in c1:
    for i in range(n):
        if len(x) > (i * 4 + 1) and x[i * 4 + 1] != ' ':
            stacks1[i].append(x[i * 4 + 1])
stacks2 = [x[:] for x in stacks1]
for o in orders:
    t = []
    for r in range(int(o[1])):
        stacks1[int(o[5]) - 1].append(stacks1[int(o[3]) - 1].pop())
        t.append(stacks2[int(o[3]) - 1].pop())
    while t:
        stacks2[int(o[5]) - 1].append(t.pop())
for i in range(n):
    print(stacks1[i][len(stacks1[i]) - 1], end='')
print()
for i in range(n):
    print(stacks2[i][len(stacks2[i]) - 1], end='')
