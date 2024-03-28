import sys
from itertools import combinations
# input=sys.stdin.readline

#최소 한 개의 모음과 최소 두 개의 자음
#뽑아서 리스트 만든 다음 combi?



L,C=map(int,input().split()) #L: 암호 길이 C:주어진 문자
lett=input().split()

combs=combinations(sorted(lett),L)

lst=[]

for comb in combs:
    m_c=0
    j_c=0

    for i in comb:
        if i in 'aeiou':
            m_c+=1
        else:
            j_c+=1

    if m_c>=1 and j_c>=2:
        print(''.join(comb))