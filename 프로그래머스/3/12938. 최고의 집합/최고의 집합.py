def solution(n, s):
    # answer = []
    
    if n>s:
        return [-1]
    elif n==s:
        return [1 for _ in range(n)]
    else: # n<s:
        std=s//n
        change=s%n
        answer=[std for _ in range(n)]
        for i in range(n):            
            if change>0:
                answer[i]+=1
                change-=1
            else:
                sorted_answer=sorted(answer)
                
                return sorted_answer