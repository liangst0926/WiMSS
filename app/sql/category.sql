SELECT
  Category.category_name AS CategoryName,
  COUNT(Product.PID) AS TotalNumberofProducts,
  AVG(Product.retail_price) AS AverageRetailPrice,
  MIN(Product.retail_price) AS MinimumRetailPrice,
  MAX(Product.retail_price) AS MaximumRetailPrice

FROM
  Category LEFT JOIN Belong ON
  Category.category_name = Belong.category_name
  LEFT JOIN Product ON Product.PID = Belong.PID

GROUP BY Category.category_name
ORDER BY Category.category_name ASC;
