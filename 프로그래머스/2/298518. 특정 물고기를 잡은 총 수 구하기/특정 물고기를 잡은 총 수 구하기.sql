-- 코드를 작성해주세요
SELECT COUNT(*) as FISH_COUNT
FROM FISH_INFO a
JOIN FISH_NAME_INFO b
ON a.FISH_TYPE=b.FISH_TYPE
WHERE b.FISH_NAME='BASS' or b.FISH_NAME='SNAPPER'
