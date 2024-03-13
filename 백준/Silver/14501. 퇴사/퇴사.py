#퇴사 전 최대로 벌기
N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
dp=[0]*(N+1)
max_v=0


for i in range(N-1,-1,-1): #i는 0-7까지
    time=i+lst[i][0]
    #퇴사일 안 넘치면
    if time<=N:
        dp[i]=max(lst[i][1]+dp[time], max_v)
        max_v=dp[i]
    else:
        dp[i]=max_v

print(max_v)