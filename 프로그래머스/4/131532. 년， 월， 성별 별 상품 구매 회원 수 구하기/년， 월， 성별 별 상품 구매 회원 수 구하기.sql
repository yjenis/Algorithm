# -- 코드를 입력하세요
# # WITH AL AS(
# #     SELECT b.online_sale_id, a.user_id, a.gender, b.sales_date, 
# #     DATE_FORMAT(b.sales_date,"%Y-%m") as DATE
# #     #YEAR(b.sales_date) as YEAR, MONTH(b.sales_date) as MONTH
# #     FROM USER_INFO a
# #     JOIN ONLINE_SALE b
# #     ON a.USER_ID=b.USER_ID
    
# # )


# # SELECT DATE, MONTH(DATE) as MONTH
# # FROM AL
# # GROUP BY DATE, MONTH(DATE)

# SELECT YEAR(sales_date), MONTH(sales_date), COUNT(GENDER=0), COUNT(GENDER=1)
# #a.gender, b.sales_date, 
# #DATE_FORMAT(b.sales_date,"%Y-%m") as DATE
# #YEAR(b.sales_date) as YEAR, MONTH(b.sales_date) as MONTH
# FROM USER_INFO a
# JOIN ONLINE_SALE b
# ON a.USER_ID=b.USER_ID
# GROUP BY YEAR(sales_date), MONTH(sales_date)

SELECT 
    YEAR(b.sales_date) AS YEAR,
    MONTH(b.sales_date) AS MONTH,
    a.gender,
    COUNT(DISTINCT a.user_id) AS USERS
FROM USER_INFO a
JOIN ONLINE_SALE b
  ON a.user_id = b.user_id
WHERE a.gender IS NOT NULL
GROUP BY YEAR(b.sales_date), MONTH(b.sales_date), a.gender
ORDER BY YEAR, MONTH, a.gender;



