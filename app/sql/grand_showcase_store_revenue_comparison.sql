CREATE OR REPLACE VIEW Store_Sold
                    AS SELECT store_number, GS_boolean, calendar_date,quantity_sold
                    FROM Store NATURAL LEFT JOIN Sold;
-- grandshowcase store data
CREATE OR REPLACE VIEW GS_Sold AS
                    SELECT calendar_date, store_number, quantity_sold FROM Store_Sold
                    WHERE GS_boolean = 1;
CREATE OR REPLACE VIEW GS_Revenue_data AS
                    SELECT YEAR(calendar_date) AS Year, store_number,quantity_sold AS Quantity, IFNULL(discount_price, retail_price) AS SoldPrice, IFNULL(percent_discount, 0)/100 AS SpecialSavingsDayDiscount
                    FROM 
                    (((GS_Sold NATURAL LEFT JOIN OnSale) NATURAL JOIN Product) NATURAL LEFT JOIN SpecialSavingsDay );
CREATE OR REPLACE VIEW GS_Revenue AS
                    SELECT Year, store_number, SUM(Quantity * SoldPrice * (1- SpecialSavingsDayDiscount)) AS TotalRevenue FROM
                    GS_Revenue_data
                    GROUP BY Year, store_number
                    ORDER BY Year;
-- regular store DATA
CREATE OR REPLACE VIEW NOGS_Sold AS
                    SELECT calendar_date, store_number, quantity_sold FROM Store_Sold
                    WHERE GS_boolean = 0;
CREATE OR REPLACE VIEW NOGS_Revenue_data AS
                    SELECT YEAR(calendar_date) AS Year, store_number,quantity_sold AS Quantity, IFNULL(discount_price, retail_price) AS SoldPrice, IFNULL(percent_discount, 0)/100 AS SpecialSavingsDayDiscount
                    FROM 
                    (((NOGS_Sold NATURAL LEFT JOIN OnSale) NATURAL JOIN Product) NATURAL LEFT JOIN SpecialSavingsDay );
CREATE OR REPLACE VIEW Store_Revenue AS
                    SELECT Year, store_number, SUM(Quantity * SoldPrice * (1- SpecialSavingsDayDiscount)) AS TotalRevenue FROM
                    NOGS_Revenue_data
                    GROUP BY Year, store_number
                    ORDER BY Year;
-- read two type stores data 
SELECT Year, COUNT(store_number) AS stores, MIN(TotalRevenue) AS minimum,
                    AVG(TotalRevenue) AS average, MAX(TotalRevenue) AS maximum, SUM(TotalRevenue) AS total FROM GS_Revenue
                    GROUP BY Year
                    ORDER BY Year;
SELECT Year, COUNT(store_number) AS stores, MIN(TotalRevenue) AS minimum,
                    AVG(TotalRevenue) AS average, MAX(TotalRevenue) AS maximum, SUM(TotalRevenue) AS total FROM Store_Revenue
                    GROUP BY Year
                    ORDER BY Year;