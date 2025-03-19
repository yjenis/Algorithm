def divde(lectures,max_size,M): #조건에 맞는
    cnt=1
    current_sum=0

    for l in lectures:
        if current_sum+l<=max_size:
            current_sum+=l
        else:
            cnt+=1
            current_sum=l
            if cnt>M:
                return False
    return True


def find_blu(N,M,lectures): #최적의 수 찾기
    low=max(lectures)
    high=sum(lectures)

    while low<=high:
        mid=int((low+high)/2)

        if divde(lectures,mid,M): #되면 줄여
            high=mid-1
        else:
            low=mid+1 #안되면 늘
    return low


N,M=map(int,input().split())
lectures=list(map(int,input().split()))

result=find_blu(N,M,lectures)
print(result)