WITH couch_sofa_revenue AS (
SELECT 
Product.PID AS ProductID, 
Product.product_name AS ProductName,
Product.retail_price AS ProductRetailPrice,
SUM(Sold.quantity_sold) AS TotalUnitsSold,
SUM(
CASE WHEN Sold.calendar_date = OnSale.calendar_date 
THEN Sold.quantity_sold ELSE 0 END) AS TotalUnitsSoldWithDiscount,
SUM(
CASE WHEN Sold.calendar_date <> OnSale.calendar_date
THEN Sold.quantity_sold ELSE 0 END) AS TotalUnitsSoldRetailPrice,
SUM(
CASE WHEN Sold.calendar_date = OnSale.calendar_date
THEN OnSale.discount_price * Sold.quantity_sold 
ELSE Product.retail_price * Sold.quantity_sold END) AS ActualRevenue,
SUM(
CASE WHEN Sold.calendar_date = OnSale.calendar_date
THEN Product.retail_price * 0.75 * Sold.quantity_sold 
ELSE Product.retail_price * Sold.quantity_sold END) AS PredictedRevenue

FROM 
Category JOIN Belong ON 
Category.category_name = Belong.category_name AND Category.category_name = 'COUCHES AND SOFAS'
JOIN Product ON Product.PID = Belong.PID
JOIN Sold ON Sold.PID = Product.PID
LEFT JOIN OnSale ON Sold.PID = OnSale.PID 
GROUP BY Product.PID
)

SELECT ProductID, ProductName, ProductRetailPrice, TotalUnitsSold, TotalUnitsSoldWithDiscount, TotalUnitsSoldRetailPrice, ActualRevenue, PredictedRevenue, (PredictedRevenue - ActualRevenue) as RevenueDifference
FROM couch_sofa_revenue
WHERE (PredictedRevenue - ActualRevenue) > 5000.00 || (PredictedRevenue - ActualRevenue) < -5000.00
ORDER BY RevenueDifference DESC; 