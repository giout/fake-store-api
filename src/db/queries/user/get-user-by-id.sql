SELECT 
    "user" AS id,
    "name",
    email,
    image_url
FROM
    "user"
WHERE
    "user" = %s::integer;