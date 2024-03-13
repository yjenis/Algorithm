R, C=map(int,input().split())
map=[list(map(str,input())) for _ in range(R)]
#빈리스트 만들어서 탐색하며 집어 넣기
lst=[]
lst2=[]
#가로로 탐색
for i in range(R):
    temp=''
    for j in range(C):

        if map[i][j]=='#':
            if len(temp)>0:
                lst.append(temp)
                temp=''
        else:
            temp+=map[i][j]

    if len(temp) > 0:
        lst.append(temp)

#세로로 탐색
for i in range(C):
    temp=''
    for j in range(R):

        if map[j][i]=='#':
            if len(temp)>0:
                lst.append(temp)
                temp=''
        else:
            temp+=map[j][i]

    if len(temp) > 0:
        lst.append(temp)

for s in lst:
    if len(s)>1:
        lst2.append(s)
lst2.sort()
print(lst2[0])