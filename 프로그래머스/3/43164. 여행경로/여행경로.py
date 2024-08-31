def solution(tickets):
    # 0. 딕셔너리로 만들기
    dict={}
    for i in tickets:
        print(i[0])
        if i[0] in dict:
            i[1]=''+i[1]
            dict[i[0]]+=(i[1])
        else:
            dict[i[0]]=(i[1])
    print(dict)