from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        print(price)
        sec = 0
        for q in queue:
            print(q)
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer