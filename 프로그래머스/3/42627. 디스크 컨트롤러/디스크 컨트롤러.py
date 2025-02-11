import heapq

def solution(jobs):
    # 요청 시간을 기준으로 정렬
    jobs.sort()
    
    n = len(jobs)  # 총 작업 개수
    time, total_time = 0, 0  # 현재 시각, 총 반환 시간
    index = 0  # jobs 리스트에서 현재 처리할 작업의 인덱스
    standby = []  # 실행 대기 중인 작업을 저장할 우선순위 큐

    while index < n or standby:
        # 현재 시간 이전에 요청된 작업을 standby에 추가
        while index < n and jobs[index][0] <= time:
            request_time, duration = jobs[index]
            heapq.heappush(standby, (duration, request_time))  # (소요 시간, 요청 시간)
            index += 1

        if standby:  # 실행 가능한 작업이 있을 경우
            duration, request_time = heapq.heappop(standby)  # 소요 시간이 가장 짧은 작업 선택
            time += duration
            total_time += time - request_time  # 반환 시간 계산
        else:  # 실행 가능한 작업이 없을 경우, 다음 작업의 요청 시간으로 이동
            time = jobs[index][0]

    return total_time // n  # 평균 반환 시간의 정수 부분 반환
