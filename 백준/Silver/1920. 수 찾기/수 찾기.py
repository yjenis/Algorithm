n=int(input())
lst=list(map(int,input().split()))
lst.sort()
m=int(input())
target=list(map(int,input().split()))

# print(lst,target)
# for t in target:
#     if t in lst:
#         print(1)
#     else:
#         print(0)

for t in target:
    find=0
    start=0
    end=n-1

    while start<=end:
        mid = int((start+end) / 2)
        if lst[mid]>t:
            end=mid-1
        elif lst[mid]<t:
            start=mid+1
        else:
            find=1
            break
    if find==1:
        print(1)
    else:
        print(0)


