# Challenge 3: Reporting With SQL: Paging Through Results (2 objectives)
## Python Techdegree
## Created by Dulio Denis on 7/21/19.

### Challenge Task 1 of 2
In a library database there's a books table. There's a title, author, genre and first_published column.

The library database is connected to a website displaying 10 books at a time, sorted by the title alphabetically.

Write a query to bring back the second page of results. Please retrieve all columns of information.

> SELECT * FROM books ORDER BY title LIMIT 10 OFFSET 10;

id	title	author	genre	first_published
4	Harry Potter and the Goblet of Fire	J.K. Rowling	Fantasy	2000
6	Harry Potter and the Half-Blood Prince	J.K. Rowling	Fantasy	2005
5	Harry Potter and the Order of the Phoenix	J.K. Rowling	Fantasy	2003

### Challenge Task 2 of 2
Imagine you're developing a Contacts application on a phone. You have a database with a phone_book table. It has the columns, first_name, last_name and phone.

The phone has a technical limitation to show 20 contacts on a screen at a time. Write the SQL query to retrieve the 3rd page of results from the phone_book table. Contacts are ordered by last name and then first name.

> SELECT * FROM phone_book ORDER BY last_name, first_name LIMIT 20 OFFSET 40;