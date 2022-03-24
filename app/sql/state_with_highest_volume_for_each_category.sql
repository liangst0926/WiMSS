SELECT DISTINCT(concat(YEAR(calendar_date), MONTH(calendar_date))) AS YearMonth
FROM Sold Order BY YearMonth;
SELECT table2.category_name, state, NumUnitSold
FROM
(SELECT category_name, MAX(TotalNum) AS NumUnitSold FROM
(SELECT state, category_name, SUM(quantity_sold) AS TotalNum
FROM Sold NATURAL JOIN Belong NATURAL JOIN Store NATURAL JOIN City
WHERE concat(YEAR(calendar_date), MONTH(calendar_date)) = %s
GROUP BY state, category_name
ORDER BY category_name, TotalNum DESC
) AS table1
GROUP BY category_name
ORDER BY category_name) AS table2,
(SELECT state, category_name, SUM(quantity_sold) AS TotalNum
FROM Sold NATURAL JOIN Belong NATURAL JOIN Store NATURAL JOIN City
WHERE concat(YEAR(calendar_date), MONTH(calendar_date)) = %s
GROUP BY state, category_name
ORDER BY category_name, TotalNum DESC
) AS table3
WHERE table2.category_name = table3.category_name AND table2.NumUnitSold = table3.TotalNum;
