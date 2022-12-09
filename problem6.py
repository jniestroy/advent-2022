f = open('problem6.txt')
a = f.readlines()[0]

letters = ''
for i in range(len(a) - 4):
    letters = a[i:i+4]
    if len(set(letters)) == 4:
        print(i + 4)
        break

letters = ''
for i in range(len(a) - 14):
    letters = a[i:i+14]
    if len(set(letters)) == 14:
        print(i + 14)
        break
