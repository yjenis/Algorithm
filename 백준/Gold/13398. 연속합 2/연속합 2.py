n=int(input())
lst=list(map(int,input().split()))
D1=[0]*(n)
D1[0]=lst[0]

D2=[0]*(n)
D2[0]=lst[0]
#D1[i] -> i번째 수를 포함한 합중 가장 큰

max_sum=lst[0]
for i in range(1,n):
    D1[i]=max(lst[i],D1[i-1]+lst[i])
    D2[i]=max(D1[i-1],D2[i-1]+lst[i])

    max_sum=max(max_sum,D1[i],D2[i])

print(max_sum)