# Challenge 3: Reporting With SQL: Paging Through Results (2 objectives)
## Python Techdegree
## Created by Dulio Denis on 7/21/19.

### Challenge Task 1 of 2
In a library database there's a books table. There's a title, author, genre and first_published column.

The library database is connected to a website displaying 10 books at a time, sorted by the title alphabetically.

Write a query to bring back the second page of results. Please retrieve all columns of information.

> SELECT * FROM books ORDER BY title LIMIT 10 OFFSET 10;

### Challenge Task 2 of 2
Challenge Server down.