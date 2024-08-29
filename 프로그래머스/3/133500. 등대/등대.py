from collections import defaultdict

def solution(n, lighthouse):
    # 트리의 인접 리스트 표현
    tree = defaultdict(list)
    for u, v in lighthouse:
        tree[u].append(v)
        tree[v].append(u)
    
    # DP 테이블 초기화
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        dp[node][1] = 1  # 노드 켜는 경우 초기값은 1
        
        for neighbor in tree[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                dp[node][0] += dp[neighbor][1]
                dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])
    
    # 1번 노드를 루트로 DFS 시작
    dfs(1)
    
    # 루트 노드의 dp 값 중 최소값이 답
    return min(dp[1][0], dp[1][1])

# 예시 실행
n = 8
lighthouse = [(1,2), (1,3), (1,4), (1,5), (5,6), (5,7), (5,8)]
print(solution(n, lighthouse))  # 출력: 2

    