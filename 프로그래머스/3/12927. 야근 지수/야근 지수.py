import heapq
#heapq.heapify(), heapq.heappush(), heapq.heappop()

def solution(n, works):
    if sum(works)<=n:
        return 0
    
    else:
        hq=[]
        for i in works: #힙으로 만들기
            heapq.heappush(hq,-i)
            # print(hq)
            
        while n>0:
            # print("꺼내기 전:",hq)
            max_num=heapq.heappop(hq) #제일 큰 수 꺼내기
            if max_num==0:
                break
            else:
                temp=max_num+1
                
                heapq.heappush(hq,temp)
                # print("꺼내서 처리후 넣음:",hq)
                n-=1
        answer=0
        for j in hq:
            answer+=j*j
            
        # print(hq)
    return answer