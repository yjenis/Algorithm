def solution(weights):
    answer = 0
    dict={}
    weights.sort()
    # for문 돌려서 딕셔너리로 만들어서 숫자 세기
    for i in weights:
        if i not in dict:
            dict[i]=0
        dict[i]+=1
    # print(dict)
    
    # dict 돌면서 1배, 2배, 3/2배, 4/3 찾기
    for i in dict:
        # 1배
        if dict[i]!=1:
            print(dict[i])
            print(i)
            n=dict[i]
            answer+=n*(n-1)/2
            # print(answer)
        # 2배
        if i*2 in dict:
            print([i,i*2])
            answer+=dict[i]*dict[i*2]
            # print(answer)
        # 3/2배
        if i*3/2 in dict:
            print([i,i*3/2])
            answer+=dict[i]*dict[i*3/2]
        # 4/3배
        if i*4/3 in dict:
            print([i,i*4/3])
            answer+=dict[i]*dict[i*4/3]
    return answer
        