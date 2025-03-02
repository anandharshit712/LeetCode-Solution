# Write your MySQL query statement below
select distinct t1.num as ConsecutiveNums
from (
    select num,
    lag(num, 1) over(order by id) as prev_value,
    lag(num, 2) over(order by id) as prev_prev_value
    from logs
) t1
where t1.num = t1.prev_value
and t1.num = t1.prev_prev_value