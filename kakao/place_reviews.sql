SELECT SUBSTRING(CREATED_AT, 6, 2) AS MONTH, COUNT(*) '후기 수'
FROM PLACE_REVIEWS
GROUP BY MONTH
ORDER BY length(MONTH), MONTH ASC;

-- 이 상태에서 한자리 수 month가 0이 붙어나온다 
-- lenth()를 사용함 