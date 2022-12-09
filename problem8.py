import numpy as np
from copy import deepcopy

f = open('problem8.txt')
a = f.readlines()
data = np.full((len(a)+2,len(a)+ 2),-1)

for i in range(len(a)):
    for j in range(len(a)):
        data[i+1][j+1] = a[i][j]

visible = []

maxs = deepcopy(data[0,:])
for i in range(1,len(a)+1):
    row_interest = data[i,:]
    coords = np.argwhere(row_interest > maxs)
    coords2 = [(i,x[0]) for x in coords]
    visible.extend(coords2)
    maxs[coords] = row_interest[coords]

maxs = deepcopy(data[:,0])
for i in range(1,len(a)+1):
    row_interest = data[:,i]
    coords = np.argwhere(row_interest > maxs)
    coords2 = [(x[0],i) for x in coords]
    visible.extend(coords2)
    maxs[coords] = row_interest[coords]


maxs = deepcopy(data[len(a) + 1,:])
for i in range(1,len(a)+1):
    row_interest = data[len(a) + 1 - i,:]
    coords = np.argwhere(row_interest > maxs)
    coords2 = [(len(a) + 1 - i,x[0]) for x in coords]
    visible.extend(coords2)
    maxs[coords] = row_interest[coords]



maxs = deepcopy(data[:,len(a) + 1])
for i in range(1,len(a)+1):
    row_interest = data[:,len(a) + 1 - i]
    coords = np.argwhere(row_interest > maxs)
    coords2 = [(x[0],len(a) + 1 - i) for x in coords]
    visible.extend(coords2)
    maxs[coords] = row_interest[coords]
print(len(set(visible)))

vis_score = 0
for i in range(1,len(a)):
    for j in range(1,len(a)):
        tree = data[i][j]
        blocked = False
        vis1 = 0
        for x in range(i + 1,len(a)+1):
            if not blocked:
                vis1 += 1
                if data[x,j] >= tree:
                    blocked = True
        blocked = False
        vis2 = 0
        for x in range(j + 1,len(a)+1):
            if not blocked:
                vis2 += 1
                if data[i,x] >= tree:
                    blocked = True
        blocked = False
        vis3 = 0
        for x in range(i - 1,0,-1):
            if not blocked:
                vis3 += 1
                if data[x,j] >= tree:
                    blocked = True
        blocked = False
        vis4 = 0
        for x in range(j - 1,0,-1):
            if not blocked:
                vis4 += 1
                if data[i,x] >= tree:
                    blocked = True
        new_vis = vis1*vis2*vis3*vis4
        if new_vis > vis_score:
            vis_score = new_vis
print(vis_score)

# vis_score = 0
# i = 4
# j = 3
# tree = data[i][j]
# maxs = -1
# vis1 = 0
# for x in range(i + 1,len(a) + 1):
#     if data[x,j] > maxs:
#         vis1 += 1
#         if data[x,j] < tree:
#             maxs = data[x,j] - 1
#         else:
#             maxs = data[x,j]
# maxs = -1
# vis2 = 0
# for x in range(j + 1,len(a) + 1):
#     if data[i,x] > maxs:
#         vis2 += 1
#         if data[i,x] < tree:
#             maxs = data[i,x] - 1
#         else:
#             maxs = data[i,x]
# maxs = -1
# vis3 = 0
# for x in range(i - 1,-1,-1):
#     if data[x,j] > maxs:
#         vis3 += 1
#         if data[x,j] < tree:
#             maxs = data[x,j] - 1
#         else:
#             maxs = data[x,j]
# maxs = -1
# vis4 = 0
# for x in range(j - 1,-1,-1):
#     if data[i,x] > maxs:
#         vis4 += 1
#         if data[i,x] < tree:
#             maxs = data[i,x] - 1
#         else:
#             maxs = data[i,x]
# new_vis = vis1*vis2*vis3*vis4
# if new_vis > vis_score:
#     vis_score = new_vis
# print(new_vis)
# vis_score = 0
# i = 4
# j = 3
# tree = data[i][j]
# blocked = False
# vis1 = 0
# for x in range(i + 1,len(a)+1):
#     if not blocked:
#         vis1 += 1
#         if data[x,j] >= tree:
#             blocked = True
# blocked = False
# vis2 = 0
# for x in range(j + 1,len(a)+1):
#     if not blocked:
#         vis2 += 1
#         if data[i,x] >= tree:
#             blocked = True
# blocked = False
# vis3 = 0
# for x in range(i - 1,0,-1):
#     if not blocked:
#         vis3 += 1
#         if data[x,j] >= tree:
#             blocked = True
# blocked = False
# vis4 = 0
# for x in range(j - 1,0,-1):
#     if not blocked:
#         vis4 += 1
#         if data[i,x] >= tree:
#             blocked = True
# new_vis = vis1*vis2*vis3*vis4
# print(vis1)
# print(vis2)
# print(vis3)
# print(vis4)
# if new_vis > vis_score:
#     vis_score = new_vis
