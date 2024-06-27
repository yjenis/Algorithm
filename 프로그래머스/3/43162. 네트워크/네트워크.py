def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]     # 방문 여부 저장 배열
    
    for com in range(n):
        if visited[com] == False:   # 1번 ~ n번 컴퓨터까지 가면서 방문하지 않은 컴퓨터라면
            DFS(n, computers, com, visited)
            answer += 1
    return answer


def DFS(n, computers, com, visited):
    visited[com] = True        # 해당 노드의 방문 여부를 True로 변경
    for i in range(n):          # 해당 노드와 연결된 다음 노드들을 모두 탐색
        if i != com and computers[i][com] == 1 and visited[i] == False:    
                DFS(n, computers, i, visited)