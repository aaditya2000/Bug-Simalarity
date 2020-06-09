issue_id = set()
component = set()
link = dict()
ans = dict()
edge = []
file = input()
file_handle = open(file, 'r')
file_handle.readline()
for line in file_handle:
    a, b = line.split(",", 1)
    b = b[:-1]
    # print(a)
    # print(b)
    issue_id.add(a)
    component.add(b)
    edge.append([b, a])

    if(a in link.keys()):
        link[a].add(b)
    else:
        link[a] = set()
        link[a].add(b)

for i in issue_id:
    for j in issue_id:
        if i != j:
            check = len(link[i].intersection(link[j]))
            if check:
                print(str(i)+"~"+str(j)+"~"+str(check))

