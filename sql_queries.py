# example queries
mysql_extract = ('''
    SELECT rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update
    FROM sakila.rental
''')

mysql_insert = ('''
    INSERT INTO sakila_duplicate.rental(rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update)
    SELECT rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update FROM sakila.rental
''')

mysql_extract = ('''
    SELECT customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update
    FROM sakila.customer
''')

mysql_insert = ('''
    INSERT INTO sakila_duplicate.customer(customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update)
    SELECT customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update FROM sakila.customer
''')

mysql_extract = ('''
    SELECT staff_id, first_name, last_name, address_id, picture, email, store_id, active, username, password, last_update
    FROM sakila.staff
''')

mysql_insert = ('''
    INSERT INTO sakila_duplicate.staff(staff_id, first_name, last_name, address_id, picture, email, store_id, active, username, password, last_update)
    SELECT staff_id, first_name, last_name, address_id, picture, email, store_id, active, username, password, last_update FROM sakila.staff
''')

mysql_extract = ('''
    SELECT store_id, manager_staff, address_id
    FROM sakila.store
''')

mysql_insert = ('''
    INSERT INTO sakila_duplicate.store(store_id, manager_staff, address_id)
    SELECT store_id, manager_staff, address_id FROM sakila.store
''')

mysql_extract = ('''
    SELECT film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update
    FROM sakila.film
''')

mysql_insert = ('''
    INSERT INTO sakila_duplicate.film(film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update)
    SELECT film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update FROM sakila.film
''')

# exporting queries
class sqlQuery:
    def __init__(self, extract_query, load_query):
        self.extract_query = extract_query
        self.load_query = load_query

# create instances for sqlQuery class
mysql_query = sqlQuery(mysql_extract, mysql_insert)

# store as list for iteration
mysql_queries = [mysql_query]
