with open('d02.ex', 'r') as f:
    d = f.readlines()
data = [x.replace('\n', '') for x in d]
s1 = s2 = 0
points1 = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6,
}
points2 = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7,
}
for x in data:
    s1 += points1[x]
    s2 += points2[x]
print('Total1:', s1)
print('Total1:', s2)
