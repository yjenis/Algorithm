# 2022년 5월 1일을 기준 1.주문 ID, 2.제품 ID, 3.출고일자, 4.출고여부
# 4. 출고여부는 2022년 5월 1일까지 출고완료로/ 이 후 날짜는 출고 대기로/ 미정이면 출고미정으로 출력

SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,"%Y-%m-%d") as OUT_DATE,
CASE 
WHEN OUT_DATE <= "2022-05-01" THEN "출고완료"
WHEN OUT_DATE > "2022-05-01" THEN "출고대기"
ELSE "출고미정"
END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC