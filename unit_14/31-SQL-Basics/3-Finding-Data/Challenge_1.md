# Challenge 1: SQL Basics: Finding the Data You Want: WHERE (3 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/7/19.

### Challenge Task 1 of 3
In our e-commerce database we have a users table with the columns id, username, password, first_name and last_name.

Write a SQL query that retrieves the first and last names only where the username is equal to "wig_lady".
> SELECT first_name, last_name FROM users WHERE username = "wig_lady";
```
irst_name 	last_name
Lola 	Love
```

### Challenge Task 2 of 3

In the products table we have the columns id, name, description and price.

Find all products that don't have the price of 9.99. Include all columns.
> SELECT * FROM products WHERE price != 9.99;
```
id 	name 	description 	price
1 	Retro Gaming T-Shirt 	All your fave gaming characters on one t-shirt. 	10.99
2 	Generic Super Hero T-Shirt 	Your fave super hero is on this shirt. Wear it. 	11.99
```

### Challenge Task 3 of 3

From the users table, find all the username fields with the last_name of "Chalkley". Only return the usernames.
> SELECT username FROM users WHERE last_name = "Chalkley";
