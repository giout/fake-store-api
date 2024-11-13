UPDATE 
    product 
SET
    "name" = %s::varchar,
    "description" = %s::varchar,
    category = %s::integer,
    image_url = %s::text,
    price = %s::numeric
WHERE 
    product = %s::integer;