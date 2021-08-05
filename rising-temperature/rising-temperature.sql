# Write your MySQL query statement below
select
    weather.Id as Id
from
    weather
        join
    weather w on datediff(weather.recordDate, w.recordDate) = 1
        and weather.Temperature > w.Temperature
;