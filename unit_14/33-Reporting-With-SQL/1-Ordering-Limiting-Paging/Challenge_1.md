# Challenge 1: Reporting With SQL: Ordering Results (3 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/15/19.

### Challenge Task 1 of 3
Imagine you're a developer on a smartphone with an embedded database. There's a phone_book table with the fields, first_name, last_name and phone. Write the SQL query to order first by last_name and then by first_name in alphabetical order.

> SELECT * FROM phone_book ORDER BY last_name, first_name;
```
id 	first_name 	last_name 	phone
6 	Brittney 	Blews 	(553)-555-9219
3 	Andrew 	Chalkley 	(679)-555-1847
4 	Lauren 	Chalkley 	(979)-555-5847
1 	Alena 	Holligan 	(590)-555-6535
2 	Elizabeth 	Kozup 	(635)-555-8583
7 	Jonathan 	Luna 	(542)-555-8703
5 	Dave 	McFarland 	(586)-555-4522
```
### Challenge Task 2 of 3

In a library database there's a books table. There's a title, author, genre and first_published column.

Order the books by the most recently published books at the top. Select all columns.

> SELECT * FROM books ORDER BY first_published DESC;
```
id 	title 	author 	genre 	first_published
13 	Armada 	Ernest Cline 	Science Fiction 	2015
11 	The Martian 	Andy Weir 	Science Fiction 	2014
18 	The Circle 	Dave Eggers 	Science Fiction 	2013
12 	Ready Player One 	Ernest Cline 	Science Fiction 	2011
7 	Harry Potter and the Deathly Hallows 	J.K. Rowling 	Fantasy 	2007
6 	Harry Potter and the Half-Blood Prince 	J.K. Rowling 	Fantasy 	2005
5 	Harry Potter and the Order of the Phoenix 	J.K. Rowling 	Fantasy 	2003
9 	The Universe in a Nutshell 	Stephen Hawking 	Non Fiction 	2001
4 	Harry Potter and the Goblet of Fire 	J.K. Rowling 	Fantasy 	2000
3 	Harry Potter and the Prisoner of Azkaban 	J.K. Rowling 	Fantasy 	1999
2 	Harry Potter and the Chamber of Secrets 	J.K. Rowling 	Fantasy 	1998
1 	Harry Potter and the Philosopher's Stone 	J.K. Rowling 	Fantasy 	1997
8 	A Brief History of Time 	Stephen Hawking 	Non Fiction 	1988
19 	Contact 	Carl Sagan 	Science Fiction 	1985
17 	Dune 	Frank Herbert 	Science Fiction 	1965
16 	1984 	George Orwell 	Fiction 	1949
20 	Animal Farm 	George Orwell 		1945
10 	Frankenstein 	Mary Shelley 	Horror 	1818
15 	Emma 	Jane Austen 	Classic 	1815
14 	Pride and Prejudice 	Jane Austen 	Classic 	1813
```
### Challenge Task 3 of 3

We're still using the library database there's a books table. There's a title, author, genre and first_published column.

Order all books by Genre and then by Title. Select all columns.

> SELECT * FROM books ORDER BY genre, title;

