from collections import deque

def solution(maps):
    # 맵 크기
    n, m = len(maps), len(maps[0])
    
    # 방문 체크 배열 (n x m 크기)
    visited = [[0] * m for _ in range(n)]
    
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    # BFS를 위한 큐 초기화 (x좌표, y좌표, 이동 거리)
    que = deque([(0, 0, 1)])  # 시작 위치 (0,0)에서 거리 1로 시작
    visited[0][0] = 1  # 시작 위치 방문 처리
    
    while que:
        x, y, cnt = que.popleft()
        
        # 상대 팀 진영 도착 시 최단 거리 반환
        if x == n - 1 and y == m - 1:
            return cnt
        
        # 네 방향 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 유효한 위치인지 확인
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1  # 방문 처리
                que.append((nx, ny, cnt + 1))  # 새로운 좌표와 이동 거리 추가
    
    return -1  # 상대 팀 진영에 도달할 수 없는 경우
