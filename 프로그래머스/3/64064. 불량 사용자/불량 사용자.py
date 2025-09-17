from itertools import product
def solution(user_id, banned_id):
    answer = 0
    # 1. banned_id별 분별
    can_lst=[]
    for i in banned_id:
        temp_lst=[]
        n=len(i)
        for j in user_id:
            Flag=True
            if n != len(j): # 일단 길이 안 맞으면 겟아웃
                continue
            else:
                for a in range(n):
                    if i[a] == '*':
                        continue
                    elif i[a]!=j[a]:
                        Flag=False
                        break
                    else:
                        continue
            if Flag:
                temp_lst.append(j)
        can_lst.append(temp_lst)

    result = set()

    # 2. DFS 탐색
    def dfs(idx, chosen):
        if idx == len(banned_id):
            result.add(frozenset(chosen))
            return 
        for u in can_lst[idx]:
            if u not in chosen:   # 중복 방지
                dfs(idx+1, chosen+[u])

    dfs(0, [])
    return len(result)
