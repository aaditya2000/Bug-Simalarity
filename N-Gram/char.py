
file =input()
file_handle=open(file,'r')

ngram=dict()
list_char=[]

for line in file_handle:
    temp=line.split(' ')
    # print(temp)
    for i in temp:
        for j in i:
            list_char.append(j)
# print(list_char)

n=len(list_char)
k=0
for i in range(2,n-1):
    word=list_char[0]
    for j in range(1,i):
        word+=list_char[j]
    ngram[i]=dict()
    ngram[i][word]=1
    ini=0
    for k in range(i,n):
        l=len(list_char[ini])
        word=word[l:]
        word+=list_char[k]
        ini+=1
        if word in ngram[i].keys():
            ngram[i][word]+=1
        else:
            ngram[i][word]=1

    # for jj in ngram[i]:
    #     print(str(jj)+" "+str(ngram[i][jj]))
    print(ngram[i])
    print("\n")





        
    
    
        
    
    
    
    

    
        
        

