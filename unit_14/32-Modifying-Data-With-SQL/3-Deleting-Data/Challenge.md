# Challenge 2: Deleting Data With SQL (3 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/14/19.

### Challenge Task 1 of 3

We have an eCommerce database and it has a products table. It has the columns id, name, description and price.

Delete all products priced at 11 or higher!

> DELETE FROM products WHERE price >= 11;

### Challenge Task 2 of 3

The same eCommerce database has a users table. It has the columns id, username, password, first_name, and last_name.

Delete the user with the username of poley_hands.

> DELETE FROM users WHERE username = "poley_hands";

### Challenge Task 3 of 3

Now we're using a database from a smartphone. It has a phone_book table. It has the columns id, first_name, last_name and phone.

Delete all contacts with the first name of Jonathan and last name of Luna.

> DELETE FROM phone_book WHERE first_name = "Jonathan" AND last_name = "Luna";
