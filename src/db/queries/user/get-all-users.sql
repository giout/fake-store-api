SELECT 
    "user" AS id,
    "name",
    email,
    image_url
FROM
    "user"
LIMIT %s::integer
OFFSET %s::integer;