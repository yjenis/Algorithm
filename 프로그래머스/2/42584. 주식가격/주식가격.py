def solution(prices):
    answer = []
    for i in range(len(prices)):
        # print(i)
        cnt=0
        for j in range(i+1,len(prices)):
            # print(j)
            cnt+=1
            if prices[i]>prices[j]:
                break
        answer.append(cnt)
    return answer