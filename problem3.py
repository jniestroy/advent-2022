f = open('problem3.txt')
a = f.readlines()

total = 0
for line in a:
    first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
    match = list(first.intersection(second))[0]
    if ord(match) >= 97:
        total += ord(match) - 96
    else:
        total += ord(match) - 38
print(total)

total = 0
i = 0
group = []
for line in a:
    group.append(set(line.replace('\n','')))
    if i % 3 == 2:
        match = list(set.intersection(*group))[0]
        if ord(match) >= 97:
            total += ord(match) - 96
        else:
            total += ord(match) - 38
        group = []
    i += 1
print(total)
