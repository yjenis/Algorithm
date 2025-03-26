import sys
input=sys.stdin.readline
from collections import Counter

n=int(input())
numbers=[int(input()) for i in range(n)]
sorted_numbers=sorted(numbers)
# print(numbers)

# 평균값
print(round(sum(numbers)/n))


# 중앙값
sorted_numbers = sorted(numbers)
median = sorted_numbers[n // 2]
print(median)



cnt=Counter(numbers)
# print(cnt)
most_common = cnt.most_common() # 정렬하
most_common.sort(key=lambda x:(-x[1],x[0]))
# print(most_common)
# print(most_common[0])

if n>=2:
    if most_common[0][1]==most_common[1][1]:
        print(most_common[1][0])
    else:
        print(most_common[0][0])
else:
    print(most_common[0][0])

# 범위
print(max(numbers)-min(numbers))