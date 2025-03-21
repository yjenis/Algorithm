import itertools
def solution(word):
     # 일단 다 만들어
    wordz=[w for w in word]
    result=[]
    lst=['A', 'E', 'I', 'O', 'U']
    for n in range(1,6):
        p_lsts=itertools.product(lst,repeat=n)
        for item in p_lsts:
            result.append(list(item))
    result.sort()
    return result.index(wordz)+1