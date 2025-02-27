n=int(input())
D=[[0]*10 for _ in range(n+1)]
for a in range(1,10):
    D[1][a]=1

for n in range(2,n+1):
    for x in range(10):
        if x==0:
            D[n][x]=D[n-1][1]
        elif x==9:
            D[n][x]=D[n-1][8]
        else:
            D[n][x]=D[n-1][x-1]+D[n-1][x+1]

print(sum(D[n])%1000000000)