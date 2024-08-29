def solution(sequence, k):
    n = len(sequence)
    left = 0
    current_sum = 0
    best_range = None

    for right in range(n):
        current_sum += sequence[right]

        # current_sum이 k를 넘을 때까지 왼쪽 포인터 이동
        while current_sum > k and left <= right:
            current_sum -= sequence[left]
            left += 1
        
        # current_sum이 k와 같을 때, 부분 수열의 길이를 확인
        if current_sum == k:
            if best_range is None or (right - left < best_range[1] - best_range[0]):
                best_range = [left, right]
            elif right - left == best_range[1] - best_range[0] and left < best_range[0]:
                best_range = [left, right]

    return best_range 