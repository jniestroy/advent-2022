f = open('problem1.txt')
a = f.readlines()

cals = []

total = 0
for i in a:
    if i != '\n':
        total += int(i)
    else:
        cals.append(total)
        total = 0

print(max(cals))
cals.sort()
print(sum(cals[-3:]))