# Challenge 7: SQL Basics: Finding the Data You Want: Pattern Matching with LIKE and % (2 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/7/19.

### Challenge Task 1 of 2
In the e-commerce database we have a products table. The columns are id, name, description and price.

Find all the products where the pattern 't-shirt' can be found anywhere in the product name.
> SELECT * FROM products WHERE name LIKE "%t-shirt%";
```
id 	name 	description 	price
1 	Retro Gaming T-Shirt 	All your fave gaming characters on one t-shirt. 	10.99
2 	Generic Super Hero T-Shirt 	Your fave super hero is on this shirt. Wear it. 	11.99
3 	Some Quirky Phrase T-Shirt 	Annoy your friends with this t-shirt. They'll seeing this phrase everytime you wear it. 	9.99
```

### Challenge Task 2 of 2

In the users table we have the columns id, username, password, first_name and last_name.

Find all users with the first name starting with the letter "L".
> SELECT * FROM users WHERE first_name LIKE "L%";
