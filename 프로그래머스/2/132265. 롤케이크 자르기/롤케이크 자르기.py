from collections import Counter
def solution(topping):
    answer = 0
    right=Counter(topping)
    left=set()
    n=len(topping)
    for i in range(n-1): #인덱스 순서
        now=topping[i]
        left.add(now) #왼쪽에 늘리고
        
        right[now]-=1 #오른쪽 빼기
        
        if right[now]==0:
            del right[now]
        
        if len(left)==len(right):
            answer+=1
        
    return answer