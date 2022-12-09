f = open('problem2.txt')
a = f.readlines()

opp = {'X':'A','Y':'B','Z':'C'}
me = {'X':1,'Y':2,'Z':3}

def result(theirs, mine):
    if theirs == opp[mine]:
        return 3
    if theirs == 'A':
        if mine == 'Z':
            return 0
        return 6
    if theirs == 'B':
        if mine == 'X':
            return 0
        return 6
    if theirs == 'C':
        if mine == 'X':
            return 6
        return 0
    
total = 0
for game in a:
    his, mine = game.replace('\n','').split(' ')
    win = result(his, mine)
    total += win + me[mine]
print(total)

new_opp = {'A':1,'B':2,'C':3}
new_me = {'X':0,'Y':3,'Z':6}
outcomes = [1,2,3]

def new_result(theirs, mine):
    if mine == 'Y':
        return new_opp[theirs]
    if mine == 'X':
        print((new_opp[theirs] - 1) - 1 % 3)
        return outcomes[((new_opp[theirs] - 1) - 1) % 3]
    if mine == 'Z':
        print((new_opp[theirs] - 1) - 1 % 3)
        return outcomes[((new_opp[theirs] - 1) + 1) % 3]
    
total = 0
for game in a:
    his, mine = game.replace('\n','').split(' ')
    win = new_result(his, mine)
    total += win + new_me[mine]
print(total)