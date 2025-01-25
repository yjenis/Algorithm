-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT, b.FISH_NAME AS FISH_NAME
FROM  FISH_INFO a
JOIN FISH_NAME_INFO b
ON a.FISH_TYPE=b.FISH_TYPE
GROUP BY b.FISH_NAME
ORDER BY FISH_COUNT DESC
