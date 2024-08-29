def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    best_range = [0, float('inf')]
    
    # right를 움직이면서 current_sum을 더하고 넘치면 left를 움직여서 빼는 게 포인트
    # left가 right를 초과해서는 안됨

    while right < len(sequence):
        if current_sum == k:
            # 현재 윈도우가 k와 같은 경우 길이 비교
            if (right - left) < (best_range[1] - best_range[0]):
                best_range = [left, right]
            elif (right - left) == (best_range[1] - best_range[0]) and left < best_range[0]:
                best_range = [left, right]

        if current_sum >= k:
            current_sum -= sequence[left]
            left += 1
        else:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]

    return best_range
