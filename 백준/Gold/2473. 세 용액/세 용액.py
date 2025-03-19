# 산성, 알칼리성
# n개의 용액들의 특성값 모두 다름, 산성이나 알칼리만 있는 경우도 있음
# 3<=n<=5000수는 10억

import sys
input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
closest_sum = float('inf')  # 0에 가장 가까운 합
result = ()  # 정답 저장할 변수

for i in range(n - 2):  # 첫 번째 용액을 고정
    left, right = i + 1, n - 1  # 두 번째, 세 번째 용액을 가리킬 포인터 설정

    while left < right:
        total = arr[i] + arr[left] + arr[right]  # 세 용액의 합

        if abs(total) < abs(closest_sum):  # 더 0에 가까운 경우 갱신
            closest_sum = total
            result = (arr[i], arr[left], arr[right])

        if total < 0:
            left += 1  # 합을 증가시키기 위해 left 이동
        elif total > 0:
            right -= 1  # 합을 감소시키기 위해 right 이동
        else:
            print(*sorted(result))  # 0이면 바로 출력하고 종료
            exit()

print(*sorted(result))  # 최종 결과 출력
