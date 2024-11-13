INSERT INTO product (
    "name",
    image_url,
    price,
    "description",
    category
) VALUES (
    %s::varchar,
    %s::text,
    %s::numeric,
    %s::varchar,
    %s::integer
) RETURNING
    product.product as id,
    product."name",
    product.image_url,
    product.price,
    product."description",
    product.category