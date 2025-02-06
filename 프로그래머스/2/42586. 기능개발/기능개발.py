from collections import deque
from math import ceil
def solution(progresses, speeds):
    answer = []
    new_lst=[]
    for i in range(len(progresses)):
        new=ceil((100-progresses[i])/speeds[i])
        new_lst.append(new)
    # print(new_lst)
    
    lst=deque(new_lst)
    # print(lst)
    
    while lst:
        std=lst.popleft()
        cnt=1
        # for i in lst:
        #     cnt+=1
        #     if std<i:
        #         break
            # else:
            #     lst.popleft()
        while lst and lst[0]<=std:
            lst.popleft()
            cnt+=1
                
            
        answer.append(cnt)       
        
    return answer