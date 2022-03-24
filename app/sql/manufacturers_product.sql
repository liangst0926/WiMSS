SELECT
  Manufacturer.manufacturer_name AS ManufacturerName,
  COUNT(PID) AS TotalNumberofProducts,
  AVG(retail_price) AS AverageRetailPrice,
  MIN(retail_price) AS MinimumNonDiscountedRetailPrice,
  MAX(retail_price) AS MaximumNonDiscountedRetailPrice
FROM
  Product RIGHT JOIN Manufacturer ON
  Product.manufacturer_name = Manufacturer.manufacturer_name
GROUP BY Manufacturer.manufacturer_name
ORDER BY AVG(retail_price) DESC
LIMIT 100;
SELECT
  Manufacturer.manufacturer_name AS ManufacturerName,
  Product.PID AS ProductID,
  Product.product_name AS ProductName,
  Product.retail_price AS NonDiscountedPrice,
  GROUP_CONCAT(DISTINCT Belong.category_name) AS Category
FROM
  Product RIGHT JOIN Manufacturer ON
  Product.manufacturer_name = Manufacturer.manufacturer_name
  LEFT JOIN Belong ON Product.PID = Belong.PID
WHERE Manufacturer.manufacturer_name = %s
GROUP BY Product.PID
ORDER BY Product.retail_price DESC;
