# 몇 시에 입양이 가장 확발하게 일어 났는지

SET @HOUR = -1;

SELECT (@HOUR :=@HOUR + 1) AS HOUR,
        (SELECT COUNT(*)
        FROM ANIMAL_OUTS
        WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;

##### 내 코드
# with h as(
#     SELECT 
#         ANIMAL_ID,DATETIME, 
#         DATE_FORMAT(DATETIME,"%H") as HOUR
#     FROM ANIMAL_OUTS
# )

# SELECT HOUR, count(*) as COUNT
# FROM h
# GROUP BY HOUR
# ORDER BY HOUR


