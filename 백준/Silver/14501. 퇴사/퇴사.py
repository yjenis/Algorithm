n=int(input())
days=[list(map(int,input().split())) for _ in range(n)]

# print(days)
D=[0]*(n+1)

for i in range(n-1,-1,-1):
    if n-i<days[i][0]:
        D[i]=D[i+1]
    else:
        nxt_idx=i+days[i][0]
        D[i]=max(D[i+1],D[nxt_idx]+days[i][1])

print(D[0])