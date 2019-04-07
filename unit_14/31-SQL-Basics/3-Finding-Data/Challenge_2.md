# Challenge 2: SQL Basics: Finding the Data You Want: >, >=, <, <= (3 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/7/19.

### Challenge Task 1 of 3
We have a database that runs a sports team's website. In the results table we have the columns id, home_team, home_score, away_team, away_score, played_on.

Find all results where the home team's score is above 12.
> SELECT * FROM results WHERE home_score > 12; 
```
id 	home_team 	home_score 	away_team 	away_score 	played_on
1 	Hessle 	45 	Rotherham 	13 	2015-09-05
3 	Hessle 	43 	Skipton 	0 	2015-09-26
```

### Challenge Task 2 of 3

We're still using the sports team's database. In the results table we have the columns id, home_team, home_score, away_team, away_score, played_on.

Find all results where the away team's score is lower than 10.
> SELECT * FROM results WHERE away_score < 10;
```
;
id 	home_team 	home_score 	away_team 	away_score 	played_on
3 	Hessle 	43 	Skipton 	0 	2015-09-26
```

### Challenge Task 3 of 3

We're back using the e-commerce database. I only have 10.99 left in my bank account. Write a query that will return all products from the products table that I can afford.

The columns in the products are id, name, description and price.
> SELECT * FROM products WHERE price <= 10.99;
