SELECT 
    "user" AS id,
    "name",
    email,
    image_url
FROM
    "user"
WHERE
    email = %s::varchar
AND
    "user" <> %s::integer;