SELECT 
    "user" AS id,
    "name",
    email,
    image_url
FROM
    "user"
LIMIT %s
OFFSET %s;