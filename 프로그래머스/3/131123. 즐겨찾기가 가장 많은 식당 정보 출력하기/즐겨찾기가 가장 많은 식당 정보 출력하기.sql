-- 코드를 입력하세요
# SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
# FROM REST_INFO
# WHERE FAVORITES IN (SELECT MAX(FAVORITES) FROM REST_INFO GROUP BY FOOD_TYPE)
# SELECT MAX(FAVORITES) FROM REST_INFO GROUP BY FOOD_TYPE
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
           ROW_NUMBER() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RN
    FROM REST_INFO
) A
WHERE RN = 1
ORDER BY 1 DESC;
