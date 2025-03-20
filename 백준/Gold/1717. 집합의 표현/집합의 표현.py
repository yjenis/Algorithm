import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])  # 경로 압축 적용
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            parents[y] = x
        else:
            parents[x] = y

def checksame(x, y):
    return find(x) == find(y)

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        print("YES" if checksame(b, c) else "NO")
