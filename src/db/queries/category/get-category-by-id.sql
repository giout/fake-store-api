SELECT 
    category AS id,
    "name",
    image_url
FROM
    category
WHERE
    category = %s;