UPDATE 
    category 
SET
    "name" = %s::varchar,
    image_url = %s::text
WHERE 
    category = %s::integer;