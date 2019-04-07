# Challenge 4: SQL Basics: Finding the Data You Want: Dates Filter (1 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/7/19.

### Challenge Task 1 of 1
We're back in the sports team database. There's a results table with the columns id, home_team, home_score, away_team, away_score and played_on .

Find all the matches in the results table where "Hessle" was playing away as the away team and if they played on or after October 1st 2015. Date format is "YYYY-MM-DD".
> SELECT * FROM results WHERE away_team = "Hessle" AND played_on >= "2015-10-01";
