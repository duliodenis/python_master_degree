# Review: Regular Expressions in Python: Final Quiz (8 Questions)
## Python Techdegree
## Created by Dulio Denis on 12/29/18.

### Quiz Question 1 of 8
Please fill in the correct answer in each blank provided below.

Fill in the blank(s) below:

    Name the following group "name".

    re.search(r'(___[\s\w]+)', 'Kenneth Love')

> ?P<name>

### Quiz Question 2 of 8

Please fill in the correct answer in each blank provided below.

Fill in the blank(s) below:

    Match the number in the string with an escape character.

    re.search(r'___', 'The Mach 5')

> \d

### Quiz Question 3 of 8

What method gives us an iterable full of match objects?

> .finditer()

### Quiz Question 4 of 8

What would I use to match 5 or more occurrences of a pattern?

> {5,}

### Quiz Question 5 of 8

Please fill in the correct answer in each blank provided below.

Fill in the blank(s) below:

    How would I get the contents of the group named email from my match object?

    match_object.___

> group('email')

### Quiz Question 6 of 8

What flag lets us write our patterns out over multiple lines, ignoring whitespace and comments?

> re.X  
> Also available as re.VERBOSE. 

### Quiz Question 7 of 8

Why would you want to compile a pattern?

> All of the Above

### Quiz Question 8 of 8

What symbol starts a set to mean "don't match any of these characters"?

> ^
