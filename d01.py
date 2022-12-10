with open('d01.ex', 'r') as f:
    content = f.read()
d1 = content.split('\n\n')
data = [x.replace('\n', ' ').split(' ') for x in d1]
ss = []
for x in data:
    s = 0
    for y in x:
        s += int(y)
    ss.append(s)
print('Most:', max(ss))
ss.sort(reverse=True)
print('Most3:', ss[0] + ss[1] + ss[2])
