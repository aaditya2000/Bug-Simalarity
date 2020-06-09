
issue_id = set()
component = set()
link = dict()
edge = []
file = input()
file_handle = open(file, 'r')
file_handle.readline()
for line in file_handle:
    a, b = line.split(",")
    b = b[:-1]

    issue_id.add(a)
    component.add(b)
    edge.append([b, a])

    if(a in link.keys()):
        link[a].add(b)
    else:
        link[a] = set()
        link[a].add(b)

ans1 = dict()

for i in issue_id:
    for j in issue_id:
        if i != j:
            check = len(link[i].intersection(link[j]))
            if check:
                if i in ans1.keys():
                    ans1[i][j] = int(check)
                else:
                    ans1[i] = dict()
                    ans1[i][j] = int(check)
                # print(i+"\t"+j+"\t"+str(check))


file1 = input()
file_handle = open(file1, 'r')
file_handle.readline()
edge1 = []
link1 = dict()
component1 = set()
issue_id1 = set()

for line in file_handle:
    a, b = line.split(",")
    b = b[:-1]

    issue_id1.add(a)
    component1.add(b)
    edge1.append([b, a])

    if(a in link1.keys()):
        link1[a].add(b)
    else:
        link1[a] = set()
        link1[a].add(b)

ans2 = dict()

# print(" -------- \n\n")
for i in issue_id1:
    for j in issue_id1:
        if i != j:
            check = len(link1[i].intersection(link1[j]))
            if check:
                if i in ans2.keys():
                    ans2[i][j] = int(check)
                else:
                    ans2[i] = dict()
                    ans2[i][j] = int(check)
                # print(i+"\t"+j+"\t"+str(check))

# print(" ------------------ \n\n")
inter = issue_id.intersection(issue_id1)

for i in issue_id:
    for j in issue_id1:
        if i == j:
            continue
        sum = 0
        for k in inter:
            if i == k or j == k:
                continue
            temp = 0
            if i in ans1.keys():
                if k in ans1[i].keys() and ans2.keys():
                    if j in ans2[k].keys():
                        a = ans1[i][k]
                        b = ans2[k][j]
                        temp = a*b
            sum = sum + temp

        print(i+"~"+j+"~"+str(sum))

