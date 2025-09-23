def solution(skill, skill_trees):
    answer = 0
    # std=[]
    # for s in skill:
    #     std.append(s)

    flag=True
    for tree in skill_trees: # n=20
        flag=True
        # print("tree:", tree)
        std2=[]
        for s in skill:
            std2.append(s)
        
        #std2=std # 초기화
        # print("기준:",std2)
        
        for i in tree: #n=26
            # print("tree중:",i)
            # print(std2)
            
            if i in std2:
                if std2.index(i)==0:
                    # print("맞아요: ",i)
                    std2.pop(0)
                    continue
                else:
                    # print("아닙니다: ",i)
                    flag=False
                    break
            else:
                # print("아무것도 아니에요")
                continue
        # print("끝났음: ",tree,flag)
        if flag==True:
            # print("+1:", tree)
            answer+=1

    return answer