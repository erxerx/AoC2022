with open('d04.ex', 'r') as f:
    d = f.readlines()
data = [[y.split('-') for y in x.replace('\n', '').split(',')] for x in d]
s1 = s2 = 0
for x in data:
    if int(x[0][0]) >= int(x[1][0]) and int(x[0][1]) <= int(x[1][1]) or int(x[0][0]) <= int(x[1][0]) and int(x[0][1]) >= int(x[1][1]):
        s1 += 1
    if not (int(x[0][1]) < int(x[1][0]) or int(x[0][0]) > int(x[1][1])):
        s2 += 1
print('Total1:', s1)
print('Total1:', s2)
