with open('names.txt') as f:
    L = []
    for line in f.readlines():
        line = line.split('\t')
        L.append(line[1].rstrip())

print(L)

myfile = open('firstnames.txt', 'w')
for name in L:
    myfile.write(name + '\n')
myfile.close()