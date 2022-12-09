f = open('problem4.txt')
a = f.readlines()

total = 0
total2 = 0 
for pair in a:
    x1, x2, y1, y2 = [int(i) for i in pair.replace('-',',').split(',')]
    range1 = set(range(x1,x2 + 1))
    range2 = set(range(y1,y2 + 1))
    if range1.issubset(range2):
        total += 1
    elif range2.issubset(range1):
        total += 1
    if range1.intersection(range2) != set():
        total2 += 1
print(total)
print(total2)
