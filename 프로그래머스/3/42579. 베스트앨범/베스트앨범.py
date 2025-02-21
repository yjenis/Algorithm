from collections import defaultdict

def solution(genres, plays):
    # 장르별로 노래들의 재생 횟수 합과 해당 노래들의 정보를 저장
    genre_play_count = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i in range(len(genres)):
        genre_play_count[genres[i]] += plays[i]
        genre_songs[genres[i]].append((plays[i], i))  # (재생 횟수, 고유번호)
    
    # 장르별로 재생 횟수 합 기준 내림차순 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)
    
    # 베스트 앨범에 들어갈 노래 고유번호를 담을 리스트
    answer = []
    
    # 각 장르 내에서 재생 횟수 기준 내림차순, 고유번호 기준 오름차순 정렬
    for genre, _ in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))  # (재생 횟수 내림차순, 고유번호 오름차순)
        
        # 베스트 앨범에는 최대 두 곡만 추가
        answer.append(songs[0][1])  # 첫 번째 노래
        if len(songs) > 1:
            answer.append(songs[1][1])  # 두 번째 노래
    
    return answer
