# This program takes raw slang files and creates dictionaries from them

File=open('slang2.txt','r')
allLines=File.readlines()
File.close()

newSlang=[]

for i in allLines:
    iter1=i.replace('~','\n')
    newSlang.append(iter1)


slangList=[]

for i in newSlang:
    slangList.append(i.split('\n'))


slangList2=[]
for i in slangList:
    for j in i:
        slangList2.append(j.split('`'))




# Creation of dictionary
def createDictionary(slangList2):
    slangDic={}
    for i in range(0,len(slangList2)):
        if slangList2[i][0]=='':
            continue
        else:
            slangDic[(slangList2[i][0]).lower()]=(slangList2[i][1].replace('+',' ')).lower()
    return slangDic

slangDictionary=createDictionary(slangList2)

def transfer():
    return slangDictionary
