n = int(input())
graph = [list(input().strip()) for _ in range(n)]

max_friends = 0

for i in range(n):
    friend_set = set()
    
    # 1-친구 추가
    for j in range(n):
        if graph[i][j] == 'Y':
            friend_set.add(j)
    
    # 2-친구 추가
    for j in range(n):
        if graph[i][j] == 'Y':  # i와 j가 친구라면
            for k in range(n):
                if graph[j][k] == 'Y' and k != i:  # j의 친구 k 추가 (단, 자기 자신 제외)
                    friend_set.add(k)
    
    max_friends = max(max_friends, len(friend_set))

print(max_friends)
