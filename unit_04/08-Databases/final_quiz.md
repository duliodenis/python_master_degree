# Review: Using Databases in Python: Final Quiz (8 Questions)
## Python Techdegree
## Created by Dulio Denis on 1/5/19.

### Quiz Question 1 of 8

You can use OrderedDict anywhere you'd use dict.
> True

### Quiz Question 2 of 8

What field type should I use if I want to store large blocks of text?
> TextField()

### Quiz Question 3 of 8

You cannot use functions as dictionary values.
> False

### Quiz Question 4 of 8

What does the os.system() function let us do?
> Use system-level utilities or applications.

### Quiz Question 5 of 8

What method lets us change how fetched records are sorted?
> order_by()

### 
Quiz Question 6 of 8

Please fill in the correct answer in each blank provided below.

I don't want to be able to have a duplicate record for UPCs in my database. Finish the model below:

class Product(Model):
    name = CharField()
    description = TextField()
    upc = CharField(max_length=100, ___=True)
> unique

### Quiz Question 7 of 8

Please fill in the correct answer in each blank provided below.

I want to sort my diary entries based on their timestamp attribute in a descending manner, so newer records are first:

Entry.select().order_by(Entry.___ . ___)

> timestamp
> desc()

### Quiz Question 8 of 8

What kind of software library is Peewee?
> ORM
