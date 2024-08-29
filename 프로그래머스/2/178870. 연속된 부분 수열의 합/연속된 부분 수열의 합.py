def solution(sequence, g):
    n = len(sequence)
    best_range = None

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += sequence[end]
            if current_sum == g:
                # 현재 부분 수열의 길이
                length = end - start
                if best_range is None or length < best_range[1] - best_range[0] or (length == best_range[1] - best_range[0] and start < best_range[0]):
                    best_range = [start, end]
                break
            elif current_sum > g:
                break

    return best_range if best_range is not None else []
