select category_name, GS_store, Non_GS_store, GS_store-Non_GS_store AS Difference from
(select category_name,
sum(CASE when GS_boolean = 1 then quantity_sold else 0 end) GS_store,
sum(CASE when GS_boolean = 0 then quantity_sold else 0 end) Non_GS_store
from
(select B.PID, B.store_number, B.category_name, B.quantity_sold, store.GS_boolean from
(select A.PID, category_name, store_number, quantity_sold from 
(select product.PID, category_name from product, belong
where product.PID = belong.PID) AS A, sold
where A.PID = sold.PID) as B, store
where B.store_number = store.store_number) as C
group by category_name) AS D
order by difference desc, category_name asc;
with myview as 
(select PID, product_name, GS_store, Non_GS_store, GS_store-Non_GS_store AS difference from
(select PID, product_name,
sum(CASE when GS_boolean = 1 then quantity_sold else 0 end) GS_store,
sum(CASE when GS_boolean = 0 then quantity_sold else 0 end) Non_GS_store 
from
(select PID, product_name, category_name, B.store_number, quantity_sold, GS_boolean from
(select A.PID, product_name, category_name, store_number, quantity_sold from
(select product.PID, product_name, category_name from product, belong
where product.PID = belong.PID) AS A, sold 
where A.PID = sold.PID) AS B, store
where B.store_number = store.store_number) AS C
where category_name = %s
group by PID) AS D)

Select PID, product_name, GS_store, Non_GS_store, difference    
from
( 
(Select *, 1 as filter
from myview 
order by difference desc, PID asc
limit 5) 

Union
(Select *, 1 as filter
from myview 
order by difference asc, PID desc
limit 5) 
order by difference desc, PID asc) as F
order by filter;
