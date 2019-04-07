# Challenge 2: SQL Basics: Getting Data from a Database (5 objectives)
## Python Techdegree
## Created by Dulio Denis on 4/6/19.

### Challenge Task 1 of 5
Here are the columns in a users table in an e-commerce site: id, username, password, first_name, last_name.

Run a SQL query to get the two columns you'd need to generate the full names of each customer.

> SELECT first_name, last_name from users;
```
first_name 	last_name
Andrew 	Chalkley
Dave 	McFarland
Pasan 	Premaratne
Lauren 	Chalkley
Rachael 	Hinkley
Lola 	Love
Nick 	Pettit
Cory 	Tepper
Jim 	Hoskins
Michael 	Poley
```

### Challenge Task 2 of 5

We're still in the e-commerce database. This time, from the products table, get the name of every product.

> SELECT name FROM products;

``` 
name
Retro Gaming T-Shirt
Generic Super Hero T-Shirt
Some Quirky Phrase T-Shirt
```

### Challenge Task 3 of 5

In the e-commerce database there's a customer_addresses table with the following columns: id, nickname, street, city, state, zip, user_id.

Select all the columns that are to do with the address. For example, all columns except id, nickname and user_id.

> SELECT street, city, state, zip FROM customer_addresses;
```
street 	city 	state 	zip
1874 24th AVE 	Lincoln City 	OR 	97233
2538 4th AVE 	Tilamook 	OR 	97242
1128 24th PL 	Portland 	OR 	97238
2325 4th ST 	Salem 	OR 	97227
3392 13th ST 	Portland 	OR 	97260
1563 3rd PL 	Tilamook 	OR 	97252
320 24th AVE 	Portland 	OR 	97256
1199 1st AVE 	Lincoln City 	OR 	97259
3411 1st PL 	Salem 	OR 	97240
1878 13th AVE 	Newport 	OR 	97249
2199 1st AVE 	Salem 	OR 	97204
958 2nd PL 	Medford 	OR 	97282
3817 13th ST 	Portland 	OR 	97230
2328 13th ST 	Lincoln City 	OR 	97231
2593 102nd ST 	Salem 	OR 	97253
3482 24th AVE 	Salem 	OR 	97256
812 103rd ST 	Salem 	OR 	97282
2772 6th PL 	Portland 	OR 	97284
3457 102nd AVE 	Newport 	OR 	97262
2487 102nd AVE 	Salem 	OR 	97296
```

### Challenge Task 4 of 5

We're using a database on a smartphone again. We have a phone_book table. In here there's an id, first_name, last_name and phone.

As the user types the phone number in we want to show possible autocomplete values. Bring back only the phone numbers of each contact only. Our smartphone can work out which of the results to show.

> SELECT phone FROM phone_book;
```
phone
(590)-555-6535
(635)-555-8583
(679)-555-1847
(586)-555-4522
(553)-555-9219
(542)-555-8703
```

### Challenge Task 5 of 5

We're still using the phone_book table. Remember it has the columns of id, first_name, last_name and phone.

Imagine a user is typing someone's last name in a search facility on the phone. As the user types, suggestions will appear on the screen. Bring back both the first name and last name for every person in the phone book. The phone will filter the appropriate suggestions.

> SELECT first_name, last_name FROM phone_book;
