with open('d06.ex', 'r') as f:
    content = f.read()
n = 4  # change into 14 for part 2
data = content.split('\n')
for s in data:
    for i in range(len(s)):
        past_set = set()
        past_set.update(s[i:i+n])
        if len(past_set) == n:
            print(i + n)
            break
