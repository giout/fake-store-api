SELECT 
    product as id,
    "description",
    image_url,
    "name",
    price,
    product 
FROM 
    product 
WHERE 
    "name" iLIKE %s || '%%' -- name
AND
    (price > COALESCE(%s, price - 1)) -- price_min
AND 
    (price < COALESCE(%s, price + 1)) -- price_max 
LIMIT %s
OFFSET %s;