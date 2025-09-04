n=int(input())
numbers=list(map(int,input().split( )))

sorted_numbers=sorted(numbers)
# print(sorted_numbers)
cnt=0
# 어떤 수가 서로 다른 두 수의 합
for now in range(n):
    target=sorted_numbers[now]
    i,j=0,n-1

    while i<j:
        if i==now:
            i+=1
            continue
        if j==now:
            j-=1
            continue

        temp=sorted_numbers[i]+sorted_numbers[j]

        if temp==target:
            cnt+=1
            break
        elif temp<target:
            i+=1
            # print('작아요: ', temp, target)
        else:
            j-=1
            # print('커요: ', temp, target)
print(cnt)