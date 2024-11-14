SELECT 
    "user" AS id,
    "name",
    email,
    image_url,
    "password"
FROM
    "user"
WHERE
    email = %s::varchar;