def solution(players, m, k):
    # m은 나누기할 기준 k는 유지시간 pop의 기준
    server=[]
    cnt=0
    idx=0
    
    # if k!=1:
    for p in players:
        # print(idx,p)
        idx+=1
        # 다음턴
        if server: # 일단 서버에 뭐가 있으면 +1을 하고, 시간 다 차면 꺼져
            # 다 찬 것 부터 가라
            server = [x for x in server if x != k]
            # print('new:',server)
            # for x in server:
                # if x==k:
                    
            server=[i+1 for i in server] # 1을하고
            # print('server',server)
            # print('1:',p,server)
            # print(p,server)
        if len(server)<int(p//m):
            n=p//m-len(server)
            for _ in range(n):
                server.append(1)
                cnt+=1
            
            # print('2:',len(server),p//m)
    return cnt