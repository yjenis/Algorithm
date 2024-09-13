n=int(input()) #세로 길이

dp=[0]*(n+1) # dp 테이블 초기화
# print(dp)

dp[0]=1
dp[1]=3

for i in range(2,n+1):
    dp[i]=(2*dp[i-1]+dp[i-2])%9901

print(dp[n])