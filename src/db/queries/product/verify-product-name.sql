SELECT 
    *
FROM 
    product
WHERE
    "name" = %s
AND
    product <> %s;