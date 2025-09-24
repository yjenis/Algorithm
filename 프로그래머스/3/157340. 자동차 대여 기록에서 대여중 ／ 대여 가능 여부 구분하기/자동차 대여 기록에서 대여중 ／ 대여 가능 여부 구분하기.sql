-- 코드를 입력하세요
# 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 대여 중이지 않은 자동차인 경우 '대여 가능'
# 차 별로 가장 최근 기록

SELECT CAR_ID,
CASE
WHEN CAR_ID IN (SELECT CAR_ID 
                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                   WHERE '2022-10-16' BETWEEN DATE_FORMAT(START_DATE,"%Y-%m-%d") and DATE_FORMAT(END_DATE,"%Y-%m-%d")) 
THEN "대여중"
ELSE "대여 가능"
END AS AVAILABILITY

FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;