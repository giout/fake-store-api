UPDATE 
    "user" 
SET
    "name" = %s::varchar,
    email = %s::varchar,
    image_url = %s::text
WHERE 
    "user" = %s::integer;