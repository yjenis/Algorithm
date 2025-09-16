def solution(n, stations, w):
    answer = 0
    cover=w*2+1
    
    for i in range(len(stations)):
        if i==0:
            front=stations[i]-w-1 # 앞부분
            if front > 0:
                std=front//cover
                change=front%cover
                # print('0번째:',front, std,change)
                if std==0:
                    answer+=1
                elif std!=0 and change==0:
                    answer+=std
                else:
                    answer+=std+1
                
        else:
            front=(stations[i]-w-1)-(stations[i-1]+w)
            std=front//cover
            change=front%cover
            # print('n번째:',front, std,change)
            if front>0:
                if std==0:
                    answer+=1
                elif std!=0 and change==0:
                    answer+=std
                else:
                    answer+=std+1
    last=stations[-1]+w
    if last<n:
        last_numz=n-last
        std_last=last_numz//cover
        change_last=last_numz%cover
        
        if change_last==0:
            answer+=std_last
        else:
            answer+=std_last+1
    else:
        return answer   
        

        
    
    return answer