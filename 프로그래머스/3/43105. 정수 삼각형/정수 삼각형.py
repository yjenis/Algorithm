def solution(triangle):
    n=len(triangle)
    # D=[[0]*n for i in range(n+1)]
    
#     for i in range(5):
#         D[5][i]=triangle[4][i]
    
    for i in range(n-2,-1,-1):
        for j in range(len(triangle[i])):
            # D[a][i]=triangle[a-1][i]+max(D[a+1][i],D[a+1][i+1])
            triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])
    # print(triangle)
    # print(D)
    return triangle[0][0]