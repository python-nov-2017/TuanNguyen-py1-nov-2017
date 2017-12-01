-- 1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.
SELECT city.city_id as city_id, city.city as city, customer.first_name as first_name, customer.last_name as last_name, customer.email as email, address.address as address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON address.city_id = city.city_id
WHERE city.city_id = 312;

-- 2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name as Genre
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE category.name LIKE "Comedy";

-- 3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.
SELECT actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) as actor_name, film.film_id, film.title, film.description, film.release_year
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address.
SELECT customer.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN store
ON customer.store_id = store.store_id
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON address.city_id = city.city_id
WHERE store.store_id = 1 AND city.city_id IN (1,42,312,459);

-- 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 15 AND rating LIKE 'G' AND special_features LIKE '%Behind the Scenes%';

-- 6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.
SELECT film.film_id, film.title, actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) as actor_name 
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- 7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features,  category.name, film.rental_rate
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE rental_rate = 2.99  AND category.name LIKE "Drama";

-- 8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
SELECT actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) as actor_name, film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE actor.first_name LIKE 'SANDRA' AND actor.last_name LIKE 'KILMER' AND category.name LIKE 'Action';