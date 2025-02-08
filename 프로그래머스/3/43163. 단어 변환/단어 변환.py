from collections import defaultdict, deque

def solution(begin, target, words):
    n=len(begin)
    words.append(begin)
    # print(words)
    if target not in words:
        return 0
    
    #구분하는 함수
    def who(a,b):
        cnt=sum([1 for f,s in zip(a,b) if f!=s])
        return cnt==1 #자체가 조건 cnt==1이면 True cnt!=1이면 False 반환    
    
    # 그래프 딕셔너리로 담기
    word_dict=defaultdict(list)
    m= len(words)
    for i in range(m):
        # print(i)
        for j in range(i+1,m):
            if who(words[i],words[j]):
                # print(words[i],words[j])
                word_dict[words[i]].append(words[j])
                word_dict[words[j]].append(words[i])
    # print(word_dict)
    
    # visted 딕셔너리로 숫자를 세기 이전 단어에 +1 숫자를 넣기
    visited={}
    # visited[begin]=0
    for i in words:
        visited[i]=0
    # print(visited)
    
    que=deque([begin])
    # print(que)
    while que:
        now=que.popleft()
        # print(now)
        if now==target:
            return visited[now]
            
        for i in word_dict[now]:
            if not visited[i]:
                que.append(i)
                visited[i]=visited[now]+1
    return 0
                
  
