class Directory:
    def __init__(self, name, parent, size = 0):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = {}
        self.files = []
        self.total_size = 0
    
    def add_file(self,size,name):
        self.size += size
        self.files.append((size,name))
    
    def add_child(self,name):
        child = Directory(name,self)
        if name in self.children.keys():
            print('Double')
        self.children[name] = child
    
    def calc_final_size(self):
        for child in self.children.keys():
            self.size += self.children[child].size

f = open('problem7.txt')
a = f.readlines()

system = Directory('',None)
system.add_child('/')
curr_dir = system
dirs = []
curr_path = []

for line in a:
    if line[0] == '$':
        command = line.split(' ')
        if command[1] == 'cd':
            dir_name = command[2].replace('\n','')
            if dir_name == '..':
                curr_dir = curr_dir.parent
                dirs.pop()
                curr_path.pop()
            else:
                curr_path.append(dir_name)
                curr_dir = curr_dir.children[''.join(curr_path)]
                dirs.append(curr_dir)
    elif line[:3] == 'dir':
        new_dir = line.split(' ')[1].replace('\n','')
        curr_dir.add_child(''.join(curr_path) + new_dir)
    else:
        file_size, file_name = line.split(' ')
        for direc in dirs:
            direc.add_file(int(file_size),file_name)

new_dirs = {}
def calc_dir_size(directory):
    size = 0
    for file in directory.files:
        size += file[0]
    for child in directory.children.keys():
        new_dirs[child] = calc_dir_size(directory.children[child])
    return size

for dir in system.children.keys():
    new_dirs[dir] = calc_dir_size(system.children[dir])

total = 0
for i in new_dirs.keys():
    if new_dirs[i] < 100000:
        total += new_dirs[i]
print(total)

total_used_space = new_dirs['/']
total_available = 70000000
curr_pathently_free = total_available - total_used_space
needed = 30000000

smallest = 1000000000
for i in new_dirs.keys():
    space_freed = new_dirs[i]
    if ((curr_pathently_free + space_freed) >= needed) and (space_freed < smallest):
        smallest = space_freed
print(smallest)
