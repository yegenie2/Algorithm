-- 코드를 입력하세요
SELECT animal_id, name, to_char(datetime, 'YYYY-MM-DD') as "날짜"
FROM animal_ins
ORDER BY animal_id;