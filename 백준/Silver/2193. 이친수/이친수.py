n=int(input())

D=[[0,0] for i in range(n+1)]
# print(D)
D[1][1]=1
# print(D)

for i in range(2,n+1):
    D[i][0]=D[i-1][0]+D[i-1][1]
    D[i][1]=D[i-1][0]

print(sum(D[n]))