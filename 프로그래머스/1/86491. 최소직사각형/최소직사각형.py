def solution(sizes):
    lg=[]
    sm=[]
    for i in sizes:
        lg.append(max(i))
        sm.append(min(i))
    # print(max(lg),max(sm))
    return max(lg)*max(sm)
    # return answer