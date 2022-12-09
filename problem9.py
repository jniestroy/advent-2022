import math
from copy import deepcopy
f = open('problem9.txt')
a = f.readlines()

start = [0,0]
h_coord = [0,0]
t_coord = [0,0]

def move_t(h,t):
    if abs(h[0] - t[0]) + abs(h[1] - t[1]) <= 1:
        return t
    elif abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) == 1:
        return t
    elif h[0] == t[0] and h[1] != t[1]:
        t[1] = (h[1] - t[1]) / 2 + t[1]
    elif h[1] == t[1] and h[0] != t[0]:
        t[0] = (h[0] - t[0]) / 2 + t[0]
    else:
        x = int(math.copysign(1,h[0] - t[0]))
        y = int(math.copysign(1,h[1] - t[1]))
        t[0] = t[0] + x
        t[1] = t[1] + y
    return t

rope = [[0,0]] * 10
coords = set()
coords2 = set()
for move in a:
    direction, distance = move.replace('\n','').split(' ')
    distance = int(distance)
    if direction == 'R':
        vec = (1,0)
    elif direction == 'U':
        vec = (0,1)
    elif direction == 'L':
        vec = (-1,0)
    else:
        vec = (0,-1)
    for step in range(distance):
        h_coord = [int(h_coord[i] + vec[i]) for i in range(2)]
        t_coord = move_t(h_coord,t_coord)
        rope[0] = [int(rope[0][i] + vec[i]) for i in range(2)]
        for i in range(1,10):
            rope[i] = move_t(deepcopy(rope[i - 1]),deepcopy(rope[i]))
        coords2.add(tuple(rope[9]))
        coords.add(tuple(t_coord))
print(len(coords))
print(len(coords2))


