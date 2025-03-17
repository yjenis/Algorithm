def count_bluerays(lectures, size):
    count = 1  # 블루레이 개수
    total = 0  # 현재 블루레이에 담긴 강의 길이 합

    for lecture in lectures:
        if total + lecture > size:  # 현재 블루레이에 더 담을 수 없는 경우
            count += 1  # 새로운 블루레이 사용
            total = lecture  # 새 블루레이에 강의 추가
        else:
            total += lecture  # 현재 블루레이에 추가
    
    return count  # 사용한 블루레이 개수 반환

def find_min_blueray_size(n, m, lectures):
    left, right = max(lectures), sum(lectures)
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 블루레이 크기의 후보
        if count_bluerays(lectures, mid) <= m:  # 블루레이 개수가 m 이하인지 확인
            answer = mid  # 가능한 크기이므로 저장
            right = mid - 1  # 더 작은 크기로 탐색
        else:
            left = mid + 1  # 크기를 키워야 함

    return answer  # 가능한 블루레이 크기 중 최소값 반환

# 입력
n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# 결과 출력
print(find_min_blueray_size(n, m, lectures))
