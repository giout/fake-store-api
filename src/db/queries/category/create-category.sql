INSERT INTO category (
    "name",
    image_url
) VALUES (
    %s::varchar,
    %s::text
) RETURNING
    category.category as id,
    category."name",
    category.image_url