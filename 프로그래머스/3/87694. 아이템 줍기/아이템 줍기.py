from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    array=[[-1]*102 for i in range(102)]
    visited=[[1]*102 for i in range(102)]
    dx=[0,0,-1,1] #상하좌우
    dy=[1,-1,0,0]
                                    
    for i in rectangle:
            x1,y1,x2,y2=map(lambda x:x*2, i) #r=요소 앞은 함수 
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    if x1<i<x2 and y1<j<y2:
                        array[i][j]=0
                    elif array[i][j] !=0: #다른 사각형 내부가 아니라면
                        array[i][j] = 1
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    que=deque([(cx,cy)])
    while que:
        x,y=que.popleft()
        if (x,y) == (ix,iy):
            return visited[x][y] //2
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if array[nx][ny]==1 and visited[nx][ny] ==1:
                visited[nx][ny]=visited[x][y]+1
                que.append((nx,ny))
                
            