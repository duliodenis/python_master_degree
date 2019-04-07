# Quiz: SQL Basics: SQL Basics: Finding the Data You Want (15 Questions)
## Python Techdegree
## Created by Dulio Denis on 4/6/19.

### Quiz Question 1 of 15
Please fill in the correct answer in each blank provided below.

I want to categorize products by price on a website. Cheap is defined by the prices from 0.01 and 9.99. Enter the missing keywords.

```SELECT name, description FROM products WHERE price __ 0.01 __ 9.99;```
> BETWEEN AND

### Quiz Question 2 of 15

You have a table full of words. You want to find all words ending with the tion at the end.

Which query would most likely display the correct results?
> SELECT word FROM words WHERE word LIKE "%tion";

### Quiz Question 3 of 15

Please fill in the correct answer in each blank provided below.

If I wanted to return rows that match either conditions, which keyword would I use?

```SELECT <columns> FROM <table> WHERE <condition 1> ___ <condition 2>;```

> OR

### Quiz Question 4 of 15

What's missing from this query to find all contacts without a phone number?

```SELECT * FROM contacts WHERE phone ___________ NULL;```

> IS

### Quiz Question 5 of 15

What's missing from this query to find all contacts with an email address present?

```SELECT * FROM contacts WHERE email _________ NULL;```

> IS NOT

### Quiz Question 6 of 15

Please fill in the correct answer in each blank provided below.

Fill in the blank(s) below:

Enter the equality operator:

```SELECT <columns> FROM <table> WHERE <column> ___ <value>;```

> =

### Quiz Question 7 of 15

Please fill in the correct answer in each blank provided below.

Fill in the missing operator. Today is 19th October 2019. I want to find all matches happening today and in the future.

```SELECT * FROM football_matches WHERE event_date  "2019-10-19";```

> \>=

### Quiz Question 8 of 15

Please fill in the correct answer in each blank provided below.

Enter the inequality operator:

```SELECT <columns> FROM <table> WHERE <column> ___ <value>;```
> !=

### Quiz Question 9 of 15

Please fill in the correct answer in each blank provided below.

What keyword is missing?

```SELECT <columns> FROM <table> ___ <condition>;```
> WHERE

### Quiz Question 10 of 15

Which operator is the greater than operator?

> \>

### Quiz Question 11 of 15

Please fill in the correct answer in each blank provided below.

If I wanted to return rows that match both conditions, which keyword would I use?

```SELECT <columns> FROM <table> WHERE <condition 1> ___ <condition 2>;```

> OR

### Quiz Question 12 of 15

Which operator is the less than operator?

> \<

### Quiz Question 13 of 15

Which keyword could you use to rewrite this query in a shorter form?

```SELECT <columns> FROM <table> WHERE <column 1> = <value 1> OR <column 1> = <value 2> OR <column 1> = <value 3>;  ```

> IN

### Quiz Question 14 of 15

Imagine you wanted to retrieve all appointments in for the upcoming week. Monday is 7th October 2019 and Friday is 11th October 2019.

Which query is the correct one to use?

> SELECT * FROM appointments WHERE day BETWEEN '2019-10-07' AND '2019-10-11';

### Quiz Question 15 of 15

What's the way to represent a missing value in SQL?

> NULL
