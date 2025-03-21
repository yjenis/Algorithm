def solution(a):
    a2=a*2 # 변수명 제일 앞에 숫자 올 수 없음
    answer=set() 
    n=len(a)
    #똑같은게 나오는 순간 멈추기
    for i in range(n): # 기준 값
        # std=a2[i]
        sum=0
        # print('1' ,i, std)
        # answer.add(std)
        for j in range(n): # 누적합
            sum+=a2[i+j]
            # print('누적합 ',j, std)
            answer.add(sum)

    # print(answer)
    return len(answer)