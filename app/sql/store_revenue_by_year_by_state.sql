SELECT DISTINCT state FROM city Order by state;
SELECT
state, store_number, street_address, city_name, YEAR(Sold.calendar_date) as soldyear,
SUM(CASE WHEN discount_price is NULL
THEN retail_price * quantity_sold *((100- IFNULL (percent_discount, 0))/100)
ELSE discount_price * quantity_sold*((100- IFNULL (percent_discount, 0))/100) END) AS Revenue
FROM
Sold natural Join Store natural Join Product
LEFT JOIN OnSale ON OnSale.calendar_date= Sold.calendar_date AND OnSale.PID= Sold.PID
LEFT JOIN SpecialSavingsDay ON SpecialSavingsDay.calendar_date = Sold.calendar_date
WHERE state = %s
GROUP BY store_number, YEAR (calendar_date)
ORDER BY YEAR(Sold.calendar_date) ASC, Revenue DESC;
