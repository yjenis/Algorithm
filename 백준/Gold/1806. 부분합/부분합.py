n, s = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0  # start와 end를 모두 0으로 초기화
now = 0
min_length = n + 1  # 최소 길이를 n+1로 설정 (최대 길이는 n)

while end < n:  # end가 배열 범위를 넘지 않도록 조건 설정
    now += numbers[end]  # 현재 구간 합에 numbers[end] 추가
    
    # 현재 구간의 합이 s 이상이면
    while now >= s:
        min_length = min(min_length, end - start + 1)  # 최소 길이 갱신
        now -= numbers[start]  # start 값을 빼고
        start += 1  # start를 오른쪽으로 이동
    
    end += 1  # end를 오른쪽으로 이동하여 새로운 값을 더함

# 최소 길이가 갱신되지 않으면 0 출력
if min_length == n + 1:
    print(0)
else:
    print(min_length)
