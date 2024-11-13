SELECT 
    *
FROM 
    product
WHERE
    "name" = %s::varchar
AND
    product <> %s::integer;