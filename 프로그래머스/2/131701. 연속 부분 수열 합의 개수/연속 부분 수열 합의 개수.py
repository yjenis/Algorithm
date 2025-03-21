def solution(a):
    a2=a*2 # 변수명 제일 앞에 숫자 올 수 없음
    answer=set() 
    n=len(a)
    #똑같은게 나오는 순간 멈추기
    for i in range(n): # 기준 값
        std=a2[i]
        # print('1' ,i, std)
        answer.add(std)
        for j in range(1,n): # 누적합
            std+=a2[i+j]
            # print('누적합 ',j, std)
            if std not in answer:
                answer.add(std)
            else:
                continue
    # print(answer)
    return len(answer)