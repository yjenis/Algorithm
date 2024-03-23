#cnt를 언제 올릴 건지

import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())

#인접리스트 만들기 위한 빈리스트
edge=[[] for _ in range(n+1)]
#방문 표시
visited=[0]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)
    # 인접 리스트 만들기


cnt=0
def dfs(start):
    # 방문 기록하기
    visited[start]=1

    for i in edge[start]:
        if visited[i]==0:
            dfs(i)

cnt=0

for c in range(1,n+1):
    if visited[c]==0:
        cnt+=1
        dfs(c)

print(cnt)