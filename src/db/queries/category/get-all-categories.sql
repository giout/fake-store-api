SELECT 
    category AS id,
    "name",
    image_url
FROM
    category
LIMIT %s
OFFSET %s;