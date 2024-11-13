SELECT 
    p.product as id,
    p."description",
    p.image_url,
    p."name",
    p.price,
    c."name" as category_name,
    c."category" as category_id,
    c."image_url" as category_image_url 
FROM 
    product p
INNER JOIN 
    category c
ON 
    p.category=c.category
WHERE   
    p.category=%s
LIMIT %s 
OFFSET %s;