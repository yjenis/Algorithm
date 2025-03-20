abz = input().strip()

count_a = abz.count('a')  # a의 개수
double_abz = abz * 2  # 원형 처리를 위해 문자열 2배 확장
n = len(abz)

# 슬라이딩 윈도우: 길이가 count_a인 연속 부분에서 b 개수 최소화
min_swaps = float('inf')
b_count = sum(1 for i in range(count_a) if double_abz[i] == 'b')  # 첫 윈도우 b 개수

min_swaps = min(min_swaps, b_count)

for i in range(1, n):  
    # 윈도우를 한 칸 오른쪽으로 이동
    if double_abz[i - 1] == 'b':
        b_count -= 1
    if double_abz[i + count_a - 1] == 'b':
        b_count += 1

    min_swaps = min(min_swaps, b_count)

print(min_swaps)
