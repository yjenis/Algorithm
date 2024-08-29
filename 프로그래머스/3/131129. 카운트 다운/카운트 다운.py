def solution(target):
    # 모든 가능한 점수들
    scores = []
    
    # 1부터 20까지 싱글, 더블, 트리플 점수 추가
    for i in range(1, 21):
        scores.append(i)          # 싱글
        scores.append(i * 2)      # 더블
        scores.append(i * 3)      # 트리플
    
    # 불 점수 추가
    scores.append(50)
    
    # DP 테이블 초기화
    dp = [(float('inf'), 0)] * (target + 1)
    dp[0] = (0, 0)  # 0점을 만드는 데는 다트 0개 필요
    
    # DP 계산
    for i in range(1, target + 1):
        for score in scores:
            if i >= score:
                # 새로운 다트 수 및 싱글/불 횟수 계산
                new_dart_count = dp[i - score][0] + 1
                new_singles_bulls = dp[i - score][1] + (1 if score <= 20 or score == 50 else 0)
                
                # 갱신 조건 확인
                if new_dart_count < dp[i][0] or (new_dart_count == dp[i][0] and new_singles_bulls > dp[i][1]):
                    dp[i] = (new_dart_count, new_singles_bulls)
    
    # 최종 결과 반환
    return list(dp[target])
