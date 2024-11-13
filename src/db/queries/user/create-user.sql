INSERT INTO "user" (
    "name",
    email,
    image_url,
    "password"
) VALUES (
    %s::varchar,
    %s::varchar,
    %s::text,
    %s::varchar
) RETURNING
    "user"."user" as id,
    "user"."name",
    "user".email,
    "user".image_url