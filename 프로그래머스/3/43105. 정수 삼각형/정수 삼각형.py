def solution(triangle):
    n = len(triangle)
    
    # 아래에서부터 거꾸로 갱신
    for i in range(n - 2, -1, -1):  # 밑에서 두 번째 줄부터 시작
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]  # 최종 최댓값
