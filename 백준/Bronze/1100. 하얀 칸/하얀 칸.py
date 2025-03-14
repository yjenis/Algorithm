chess=[list(map(str,input())) for _ in range(8)]
# print(len(chess),len(chess[0]))
array=[]
e1=[1,0,1,0,1,0,1,0]
e2=[0,1,0,1,0,1,0,1]
for _ in range(4):
    array.append(e1)
    array.append(e2)
# print(array)
# print(len(array),len(array[0]))
cnt=0

for i in range(8):
    for j in range(8):
        # print(array[i][j], chess[i][j])
        if array[i][j]==1 and chess[i][j]=='F':
            cnt+=1

print(cnt)