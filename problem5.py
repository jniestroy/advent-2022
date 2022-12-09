towers = [
    ['W','R','F'],
    ['T','H','M','C','D','V','W','P'],
    ['P','M','Z','N','L'],
    ['J','C','H','R'],
    ['C','P','G','H','Q','T','B'],
    ['G','C','W','L','F','Z'],
    ['W','V','L','Q','Z','J','G','C'],
    ['P','N','R','F','W','T','V','C'],
    ['J','W','H','G','R','S','V']
]

# towers = [
#     ['Z','N'],
#     ['M','C','D'],
#     ['P']
# ]

def pop_last(l,k):
    l, last = l[:len(l) - k], l[-k:]
    return l, last

def move_from(a,b,n):
    a, last = pop_last(a,n)
    #last.reverse() #comment out for part 2
    b.extend(last)
    return a, b


f = open('problem5.txt')
a = f.readlines()

i = 0
for shuffle in a:
    move = int(shuffle.split('move ')[1].split(' ')[0]) 
    fro = int(shuffle.split('from ')[1].split(' ')[0]) - 1
    to = int(shuffle.split('to ')[1].split(' ')[0]) - 1
    towers[fro], towers[to] = move_from(towers[fro],towers[to],move)

for tower in towers:
    print(tower[-1])

