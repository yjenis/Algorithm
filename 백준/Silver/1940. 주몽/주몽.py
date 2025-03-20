n=int(input())
m=int(input())
numbers=list(map(int,input().split()))
numbers.sort()
cnt=0
start=0
end=n-1

while start<end:
    if numbers[start]+numbers[end]==m:
        cnt+=1
        start+=1
        
    elif numbers[start]+numbers[end]<m:
        start+=1
    else:
        end-=1
print(cnt)