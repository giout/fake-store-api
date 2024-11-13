SELECT 
    category AS id,
    "name",
    image_url
FROM
    category
WHERE
    "name" = %s::varchar
AND
    category <> %s::integer;