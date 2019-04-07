# Challenge 8: SQL Basics: Finding the Data You Want: Filtering IS NULL, IS NOT NULL (2 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/7/19.

### Challenge Task 1 of 2
We're back on the smartphone, but our phone_book is a mess. There's a phone_book table but there's missing information in a couple of the columns.

The phone_book has the following columns id, first_name, last_name and phone.

Find all contacts in the phone_book where the phone number is missing so we can go and ask them for their number.
> SELECT * FROM phone_book WHERE phone IS NULL;
```
id 	first_name 	last_name 	phone
2 	Elizabeth 	Kozup 	
4 	Dave 	McFarland 	
```

### Challenge Task 2 of 2

We're still using the phone_book, with the columns id, first_name, last_name and phone.

Imagine we're implementing the autocomplete feature for a search facility on the phone where a user can start typing a last name and suggestions will appear. Write a query to retrieve all values from the last name column where the last name value is present. Only retrieve the last_name column.
> SELECT last_name FROM phone_book WHERE last_name IS NOT NULL;
