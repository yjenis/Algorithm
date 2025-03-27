import copy
from itertools import combinations
from collections import deque


n,m=map(int,input().split())
max_cnt=0
arr=[list(map(int,input().split())) for _ in range(n)]

wall=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]

# 벽 세우기 로직 없이 완탐으로
just=[]
Q=deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            just.append([i,j])
        elif arr[i][j] == 2:
            Q.append((i, j))  # 바이러스 위치 저장

wall=list(combinations(just,3))

def bfs(arr):
    temp_Q = deque(Q)  # 원본을 유지하기 위해 복사
    while temp_Q:
        y, x = temp_Q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[ny][nx] == 0:  # 빈 칸이면 감염
                    arr[ny][nx] = 2
                    temp_Q.append((ny, nx))

for walls in wall:
    arr2 = copy.deepcopy(arr)
    # print('arr2',arr2)
    for y,x in walls:
        arr2[y][x]=1
    bfs(arr2)
    max_cnt = max(sum(row.count(0) for row in arr2), max_cnt)
    # 벽 세웠음
    # temp_Q = deque(Q)
    # while temp_Q:
    #     y,x=temp_Q.popleft()
    #     for d in range(4):
    #         nx,ny= x+dx[d],y+dy[d]
    #         if 0<=nx<m and 0<=ny<n:
    #             if arr2[ny][nx]==0:
    #                 arr2[ny][nx]=2
    #                 temp_Q.append([ny,nx])
    #             elif arr2[ny][nx]==1:
    #                 break
    #             else:
    #                 continue
    #         else:
    #             continue
    # print(arr2)
    # print(max_cnt)



print(max_cnt)


