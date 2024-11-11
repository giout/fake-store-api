CREATE TABLE public.category (
	category serial4 NOT NULL,
	"name" varchar(100) NOT NULL,
	image_url text NOT NULL,
	CONSTRAINT category_pkey PRIMARY KEY (category),
	CONSTRAINT unq_category UNIQUE (name)
);

CREATE TABLE public.product (
	product serial4 NOT NULL,
	"name" varchar(100) NOT NULL,
	description varchar(200) NOT NULL,
	price numeric NOT NULL,
	image_url text NOT NULL,
	category int4 NOT NULL,
	CONSTRAINT product_pkey PRIMARY KEY (product),
	CONSTRAINT unq_product UNIQUE (name)
);
ALTER TABLE public.product ADD CONSTRAINT product_category_fkey FOREIGN KEY (category) REFERENCES public.category(category) ON DELETE CASCADE;

CREATE TABLE public."user" (
	"user" serial4 NOT NULL,
	"name" varchar(100) NOT NULL,
	"password" varchar(200) NOT NULL,
	email varchar(200) NOT NULL,
	image_url text NOT NULL,
	CONSTRAINT user_pkey PRIMARY KEY ("user")
);