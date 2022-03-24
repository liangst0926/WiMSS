CREATE OR REPLACE VIEW City_Category
                    AS SELECT state, city_name,
                    CASE
                    WHEN city_population < 3700000 THEN 'Small'
                    WHEN city_population < 6700000 THEN 'Medium'
                    WHEN city_population < 9000000 THEN 'Large'
                    ELSE 'Extra Large'
                    END AS CityCategory
                    FROM City;
CREATE  OR REPLACE VIEW RevenueByPopulation AS
                    SELECT Year, CityCategory, SUM(Quantity*SoldPrice*SpecialSavingsDayDiscount) AS TotalRevenue
                    FROM
                    (SELECT YEAR(calendar_date) AS Year, CityCategory, quantity_sold AS Quantity, IFNULL(discount_price, retail_price) AS SoldPrice, (1-IFNULL(percent_discount/100, 0)) AS SpecialSavingsDayDiscount
                    FROM (((((Sold NATURAL LEFT JOIN OnSale) NATURAL JOIN Product) NATURAL LEFT JOIN SpecialSavingsDay ) NATURAL JOIN Store) NATURAL JOIN City_Category)
                    ) AS T
                    GROUP BY Year, CityCategory
                    ORDER BY Year, FIELD(CityCategory, 'Small', 'Medium', 'Large', 'Extra Large');            
 SELECT Year,
                    SUM(CASE WHEN CityCategory = 'Small' Then TotalRevenue END) AS 'Small',
                    SUM(CASE WHEN CityCategory = 'Medium' Then TotalRevenue END) AS 'Medium',
                    SUM(CASE WHEN CityCategory = 'Large' Then TotalRevenue END) AS 'Large',
                    SUM(CASE WHEN CityCategory = 'Extra Large' Then TotalRevenue END) AS 'Extra Large'
                    FROM RevenueByPopulation
                    GROUP BY Year;
