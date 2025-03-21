def solution(n, times):
    start,end=1,n*max(times)
    answer=[]
    
    while start<=end:
        mid=int((end+start)/2)
        total = sum(mid // t for t in times)

        if total>=n:
            answer.append(mid)
            end=mid-1
        else:
            start=mid+1

    return min(answer)
    