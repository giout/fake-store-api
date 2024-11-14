UPDATE 
    "user" 
SET
    "password" = %s::varchar
WHERE 
    "user" = %s::integer;