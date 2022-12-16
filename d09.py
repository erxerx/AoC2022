from operator import add, sub


def square(x):
    return x*x


with open('d09.in', 'r') as f:
    d = f.readlines()
motions = [x.replace('\n', '').split(' ') for x in d]
head = tail = [0, 0]
places = []
delta = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
for m in motions:
    for i in range(int(m[1])):
        head = list(map(add, head, delta[m[0]]))
        if sum(map(square, map(sub, head, tail))) < 4: continue
        if tail[0] < head[0]: tail[0] += 1
        if tail[0] > head[0]: tail[0] -= 1
        if tail[1] < head[1]: tail[1] += 1
        if tail[1] > head[1]: tail[1] -= 1
        if tail not in places: places.append(tail.copy())
print(len(places) + 1)

# 6091 too high
