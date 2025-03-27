-- 코드를 입력하세요
SELECT a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY, sum(c.SALES*a.PRICE) as TOTAL_SALES
FROM BOOK a
JOIN AUTHOR b ON a.AUTHOR_ID=b.AUTHOR_ID
RIGHT JOIN BOOK_SALES c ON a.BOOK_ID=c.BOOK_ID
WHERE YEAR(c.SALES_DATE)=2022 and MONTH(c.SALES_DATE)=01
GROUP BY a.AUTHOR_ID, a.CATEGORY
ORDER BY a.AUTHOR_ID, a.CATEGORY DESC