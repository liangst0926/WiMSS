SELECT Year1 AS Year, TotalNumSold, AveNumSold, GroundhogSold
FROM
(SELECT Year AS Year1, SUM(quantity_sold) AS TotalNumSold, (SUM(quantity_sold)/365) AS AveNumSold
FROM
(SELECT YEAR(calendar_date) AS Year, quantity_sold FROM sold Natural JOIN belong WHERE category_name = %s ) As table1
GROUP BY Year
ORDER BY Year) AS table2
LEFT JOIN
(SELECT Year AS Year2, SUM(quantity_sold) AS GroundhogSold
FROM
(SELECT YEAR(calendar_date) AS Year, quantity_sold FROM sold Natural JOIN belong WHERE category_name = %s AND MONTH(calendar_date) = 2 AND DAY(calendar_date) = 2) AS table3
GROUP BY Year
ORDER BY Year) AS table4
ON table2.Year1 = table4.Year2;