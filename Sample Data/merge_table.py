dekh = dict()
n = 0


def check(file, i):
    fo = open(file, 'r')
    # print(file)
    for line in fo:
        # print(line)
        a, b, c = line.split('~')
        a = a+","+b
        c = c[:-1]
        if a in dekh.keys():
            dekh[a][i] = c
        else:
            dekh[a] = ['0']*n
            dekh[a][i] = c


file = "input.txt"
file_handle = open(file, 'r')

for line in file_handle:
    n += 1

file_handle.seek(0, 0)
i = 0
for line in file_handle:
    text = line[:-1]
    check(text, i)
    i += 1

print("source,dest", end="")
file_handle.seek(0, 0)
for line in file_handle:
    line = line[:-1]
    print(","+line, end="")
print()
for i in dekh:
    print(i, end="")
    for j in dekh[i]:
        print(","+j, end="")
    print()
