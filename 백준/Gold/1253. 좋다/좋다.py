n=int(input())
numbers=list(map(int,input().split()))
numbers.sort()
cnt=0


#인덱스로 풀기

for i in range(n):
    target=numbers[i]
    left,right=0,n-1

    while left<right:
        if left==i:
            left+=1
            continue
        if right==i:
            right-=1
            continue

        if numbers[left]+numbers[right]==target:
            if left != right:
                cnt+=1
                break

        elif numbers[left]+numbers[right]<target:
            left+=1
        else:
            right-=1

print(cnt)