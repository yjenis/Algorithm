# 사원별 성과금 정보 조회
# 사번, 성명, 평가 등급, 성과금을 조회
SELECT a.EMP_NO, a.EMP_NAME,
CASE
    WHEN avg(SCORE)>=96 THEN 'S'
    WHEN avg(SCORE)>=90 THEN 'A'
    WHEN avg(SCORE)>=80 THEN 'B'
    ELSE 'C'
END as GRADE,

CASE
WHEN avg(SCORE)>=96 THEN a.SAL*0.2
WHEN avg(SCORE)>=90 THEN a.SAL*0.15
WHEN avg(SCORE)>=80 THEN a.SAL*0.1
ELSE 0
END as BONUS

FROM HR_EMPLOYEES a
JOIN HR_GRADE b
ON a.EMP_NO=b.EMP_NO

GROUP BY a.EMP_NO

ORDER BY a.EMP_NO