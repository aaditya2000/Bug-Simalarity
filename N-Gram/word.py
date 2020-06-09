file = input()
file_handle=open(file,'r')

ngram=dict()
list_word=[]

for line in file_handle:
    temp=line.split(' ')
    # print(temp)
    list_word+=temp
# print(list_word)

n=len(list_word)
k=0
for i in list_word:
    print(i,end=" ")
print("\n")
for i in range(2,8):
    word=list_word[0]
    for j in range(1,i):
        word+="_"+list_word[j]
    ngram[i]=dict()
    ngram[i][word]=1
    ini=0
    for k in range(i,n):
        l=len(list_word[ini])+1
        word=word[l:]
        word+="_"+list_word[k]
        ini+=1
        if word in ngram[i].keys():
            ngram[i][word]+=1
        else:
            ngram[i][word]=1

    # for jj in ngram[i]:
    #     print(str(jj)+" "+str(ngram[i][jj]))
    # print("\n")
    for jj in ngram[i]:
        print(str(jj),end=" ")
    print("\n")





        
    
    
        
    
    
    
    

    
        
        

