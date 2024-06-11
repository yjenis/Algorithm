def solution(clothes):
    answer = 1
    hanger_dict = {}
    
    for clo in clothes :
        if clo[1] not in hanger_dict.keys() :
            # 위장할 종류(clo[1])가 딕셔너리에 없으면
            hanger_dict[ clo[1] ] = 1
        else :
            # 위장할 종류(clo[1])가 딕셔너리에 이미 있으면
            hanger_dict[ clo[1] ] += 1
    
    for key, value in hanger_dict.items() :
        answer *= ( value + 1 ) 
        # ( value : 위장하기 위해 입는 경우의 수 ) + ( 1 : 안 입는 경우 )
        # * : 여러 종류 옷들의 조합의 수를 구하기 위해 곱해준다
        
    answer -= 1
    # -1 : 모든 종류의 옷을 안 입는 경우도 count 되었으므로 빼준다
        
    return answer
