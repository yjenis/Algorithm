# 서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문
# 리뷰 평균점수는 소수점 세 번째 자리에서 반올림
# 평균점수를 기준으로 내림차순 정렬해주시고, 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬

# 리뷰 평점이 핵심


WITH SC as (SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) as SCORE
FROM REST_REVIEW 
GROUP BY REST_ID)

SELECT DISTINCT a.REST_ID, a.REST_NAME, a.FOOD_TYPE,a.FAVORITES,a.ADDRESS,c.SCORE
FROM REST_INFO a
JOIN REST_REVIEW b
ON a.REST_ID=b.REST_ID
JOIN SC c
ON a.REST_ID=c.REST_ID
WHERE ADDRESS LIKE "서울%"
ORDER BY c.SCORE DESC, a.FAVORITES DESC

