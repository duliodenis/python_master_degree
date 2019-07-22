# Challenge 2: Reporting With SQL: Limiting Results (2 objectives)
## Python Techdegree
## Created by Dulio Denis on 7/21/19.

### Challenge Task 1 of 2
We're using the library database again. There's a books table. There's a title, author, genre and first_published column.

Write a query to obtain the first 5 books in the Fantasy genre ordered by the year released. Oldest first. Select all columns.

> SELECT * FROM books WHERE genre='Fantasy' ORDER BY first_published ASC LIMIT 5;
id	title	author	genre	first_published
1	Harry Potter and the Philosopher's Stone	J.K. Rowling	Fantasy	1997
2	Harry Potter and the Chamber of Secrets	J.K. Rowling	Fantasy	1998
3	Harry Potter and the Prisoner of Azkaban	J.K. Rowling	Fantasy	1999
4	Harry Potter and the Goblet of Fire	J.K. Rowling	Fantasy	2000
5	Harry Potter and the Order of the Phoenix	J.K. Rowling	Fantasy	2003

### Challenge Task 2 of 2
We're still using the library database with the books table. There's a title, author, genre and first_published column.

Find the earliest Science Fiction book in our library. Only one result should be returned. All columns should be selected.

> SELECT * FROM books WHERE genre="Science Fiction" ORDER BY first_published ASC LIMIT 1;
