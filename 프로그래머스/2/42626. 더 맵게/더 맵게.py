import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0

    # 모든 음식의 스코빌 지수가 K 이상일 때
    while len(scoville)>1 and scoville[0]<K:
            # print(scoville)
            a=heapq.heappop(scoville)
            # print(scoville)
            b=heapq.heappop(scoville)
            # print(scoville)
            heapq.heappush(scoville,a+b*2)
            cnt+=1
    if scoville[0]<K:
            return -1

            
        
    return cnt
        