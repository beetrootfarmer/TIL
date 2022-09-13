-- 가장 많은 후기를 남긴 유저의 아이디
-- 같은 수의 후기를 남겼다면 여러개 표출

SELECT a.REVIEWER_ID USER_ID
FROM PLACE_REVIEWS a
    , (SELECT count(ID) AS cnt, REVIEWER_ID
        FROM PLACE_REVIEWS
        GROUP BY REVIEWER_ID
        HAVING cnt > 1 -- max(cnt)로 했을 때 id 정렬이 안되어서 2가 max이길래 이렇게 함
    )b 
WHERE a.REVIEWER_ID = b.REVIEWER_ID 