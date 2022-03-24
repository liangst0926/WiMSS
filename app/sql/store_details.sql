SELECT manage.store_number AS "Store Number", street_address AS "Street Address", phone_number AS "Phone Number",    
CASE GS_boolean
when 1 then "YES"
else "No" 
END "Grand Showcase Store?"
FROM Manage LEFT JOIN Store ON Manage.store_number = Store.store_number 
WHERE user_name = %s


