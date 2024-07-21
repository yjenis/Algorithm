def solution(k, tangerine):
    
    # 딕셔너리 만들기
    my_dict={}
    
    for i in tangerine:
        if i not in my_dict:
            my_dict[i]=0
        my_dict[i]+=1
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    

    #개수 셀 카운트
    cnt=0
    total=0
    
    for value in sorted_dict.values():
        
        if total<k:
            total+=value
            cnt+=1
            
        else:
            break
    return cnt
    
        
        