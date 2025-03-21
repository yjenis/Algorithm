# 10일동안 살 수 있고 하루에 한 품목씨 하나만 살 수 있음
from collections import defaultdict

def solution(want, number, discount):
    n=len(want)
    m=len(discount)
    food=defaultdict(int)
    cnt=0
    for i in range(n):
        food[want[i]]+=number[i]
    
    for s in range(m-10+1): #윈도우 출발점 정하기
        mart=defaultdict(int)
        for j in range(s,s+10): #거기부터 10개 딕셔너리 만들기
            mart[discount[j]]+=1
        # print(mart)
        if food==mart:
            cnt+=1
        #     print('yes',food,mart)
        # else:
        #     print('no',food,mart)

    return cnt
