# Challenge 2: Reporting With SQL: Limiting Results (2 objectives)
## Python Techdegree
## Created by Dulio Denis on 7/21/19.

### Challenge Task 1 of 2
We're using the library database again. There's a books table. There's a title, author, genre and first_published column.

Write a query to obtain the first 5 books in the Fantasy genre ordered by the year released. Oldest first. Select all columns.

> SELECT * FROM books WHERE genre='Fantasy' ORDER BY first_published ASC LIMIT 5;

### Challenge Task 2 of 2
Challenge Server down.