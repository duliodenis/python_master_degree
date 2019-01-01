# Original JavaScript
"""
alert("script connected!");
var age = prompt("What is your age?");

if (age === 21) {
	console.log("Happy 21st Birthday!") 
}
else if (Math.sqrt(age) * Math.sqrt(age) === age) {
	console.log("Perfect Square!") 
}
else if (age % 2 !=== 0) {
	console.log("You're odd!")
}

else if (age < 0) {
	console.log("I'm sorry, but your age cannot be negative");
}
else {
	console.log("You are " + age + " years old.");
}
"""

import math

def agefunction(age):
    square_age = math.sqrt(age)
    if age == 21:
        print("Happy 21st")
    elif square_age*square_age == age:
        print("A perfect square")
    elif age % 2 != 0:
        print("You're odd.")
    elif age < 0:
        print("You can't be less than zero.")
    else:
        print("You are {} years old".format(age))

age = int(input("What is your age? >"))
agefunction(age)
