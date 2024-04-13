
import sys
input=sys.stdin.readline
import itertools
from itertools import combinations

T=int(input())

for tc in range(1,T+1):
    # 조건 받기
    n=int(input())
    mbti=list(map(str,input().split()))
    if n>32:
        print(0)
    # 조합 만들기
    else:
        comb=list(combinations(mbti,3))
        # print(comb)
        # 비교 값
        max_v=10000

        for num in comb:
            #cnt 초기화
            cnt=0

            # A와 B 사이의 심리적 거리
            for i in range(4):
                if num[0][i]!=num[1][i]:
                    cnt+=1
            # B와 C 사이의 심리적 거리
            for i in range(4):
                if num[1][i] != num[2][i]:
                    cnt += 1
            # A와 C 사이의 심리적 거리
            for i in range(4):
                if num[0][i] != num[2][i]:
                    cnt += 1

            if max_v>cnt:
                max_v=cnt

        print(max_v)