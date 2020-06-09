file = "stammed_input.txt"

file_handle = open(file, 'r')

file_handle.readline()
f = []
for i in range(0, 8):
    te = "ngram_"+str(i)+".txt"
    f.append(open(te, 'w'))
    f[i].write("issue_id,topic_ngram\n")
for line in file_handle:
    ngram = dict()
    list_word = []
    a, temp = line.split('~', 1)
    temp = temp[:-1]
    temp = temp.split(' ')
    temp = temp[:-1]
    list_word += temp
    n = len(list_word)
    k = 0
    # for 1gram
    for i in list_word:
        te = str(a)+","+str(i)+"\n"
        f[1].write(te)
        # print(a+","+i)

    for i in range(2, min(8, n+1)):
        word = list_word[0]
        for j in range(1, i):
            word += "_"+list_word[j]
        ngram[i] = dict()
        ngram[i][word] = 1
        ini = 0
        for k in range(i, n):
            l = len(list_word[ini])+1
            word = word[l:]
            word += "_"+list_word[k]
            ini += 1
            if word in ngram[i].keys():
                ngram[i][word] += 1
            else:
                ngram[i][word] = 1
        for jj in ngram[i]:
            te = str(a)+","+str(jj)+"\n"
            f[i].write(te)

for i in range(0, 8):
    f[i].close()
