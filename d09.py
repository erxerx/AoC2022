from operator import add, sub


def square(x):
    return x * x


def onemove(lh, lt):
    if sum(map(square, map(sub, lh, lt))) >= 4:
        if lt[0] < lh[0]: lt[0] += 1
        if lt[0] > lh[0]: lt[0] -= 1
        if lt[1] < lh[1]: lt[1] += 1
        if lt[1] > lh[1]: lt[1] -= 1
    return lh, lt


delta = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
with open('d09.ex', 'r') as f:
    d = f.readlines()
motions = [x.replace('\n', '').split(' ') for x in d]
head = tail = [0, 0]
places = [[0, 0]]
for m in motions:
    for j in range(int(m[1])):
        head = list(map(add, head, delta[m[0]]))
        head, tail = onemove(head, tail)
        if tail not in places: places.append(tail.copy())
print(len(places))

rope = [[0, 0] for x in range(10)]
places = [[0, 0]]
for m in motions:
    for i in range(int(m[1])):
        rope[0] = list(map(add, rope[0], delta[m[0]]))
        for j in range(len(rope) - 1):
            rope[j], rope[j + 1] = onemove(rope[j], rope[j + 1])
        if rope[9] not in places: places.append(rope[9].copy())
print(len(places))
