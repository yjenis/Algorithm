n,m=list(map(int,input().split()))
# arr=[list(map(int,input())) for _ in range(n)]
D=[[0]*1001 for i in range(1001)]
# D2=[[0 for j in range(10)] for i in range(10)]
# print(D1)
max=0
# 위 i-1,j 왼쪽 i,j-1, 대각선 왼쪽 위 i-1,j-1
for i in range(n):
    arr=list(input())
    # print(arr)
    for j in range(m):
        D[i][j]=int(arr[j])
        if D[i][j]==1 and i>0 and j>0:
            D[i][j]=min(D[i-1][j],D[i][j-1],D[i-1][j-1])+1
        if max < D[i][j]:
            max=D[i][j]
print(max*max)
