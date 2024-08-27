import sys
def solution(target):

    n = max(61, target+1)
	
    # d[i] : [i 점수를 맞출 때 맞춘 최소 수, 싱글이거나 불 횟수]
    d = [[target, 0] for _ in range(n)]  # 조합수, 싱글, 불 개수

    d[50] = [1, 1] # 불 

    for i in range(1, 21): # 1~60 (싱글, 더블, 트리플)
        if 1<=i<= 20:
            d[i]=[1, 1]
        if d[i*2] == [target, 0]:
            d[i*2] = [1, 0]
        if d[i*3] == [target, 0]:
            d[i*3] = [1, 0] 

    for i in range(23, n):
        single = [] # 싱글, 불

        for j in range(1, 61):
            if d[i-j][0] + d[j][0] <= d[i][0]: # 새로 맞추는거랑 원래 개수랑 비교
                d[i][0] = d[i-j][0] + d[j][0] # 최솟값으로 설정
                single.append([d[i-j][0] + d[j][0], d[i-j][1] + d[j][1]])

        single.sort(key=lambda x: [x[0], -x[1]])

        if len(single) > 0:
            d[i] = single[0]

    return d[target]