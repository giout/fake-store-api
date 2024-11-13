SELECT 
    category AS id,
    "name",
    image_url
FROM
    category
LIMIT %s::integer
OFFSET %s::integer;