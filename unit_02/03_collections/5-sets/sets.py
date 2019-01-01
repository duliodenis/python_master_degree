#
#  Experiments with Sets
#  Python Techdegree
#
#  Created by Dulio Denis on 12/11/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 3
#  ---------------------
#  I think it's a good idea for you to experiment with sets since they're a very useful part of Python.
#  Start by creating a set variable named songs that has three song titles in it. 
#  You can use any titles you want, just make sure they're three different strings.
songs = {"Love It If We Made It", "Honey", "Malamente "}
print(songs)
print("-"*40)

# Challenge Task 2 of 3
# ---------------------
# Awesome. Now use the .add() method to add the title "Treehouse Hula" to songs.
songs.add("Treehouse Hula")
print(songs)
print("-"*40)

# Challenge Task 3 of 3
# ---------------------
# Alright, and last task. Use .update() to add the following two sets to your songs set.
# {"Python Two-Step", "Ruby Rhumba"}
# {"My PDF Files"}
songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})
print(songs)
print("-"*40)

# ---------------------
# Challenge Task 1 of 2
# ---------------------
# Let's write some functions to explore set math a bit more. 
# We're going to be using this COURSES dict in all of the examples. Don't change it, though!
# So, first, write a function named covers that accepts a single parameter, a set of topics. 
# Have the function return a list of courses from COURSES where the supplied set and the course's value (also a set) overlap.
# For example, covers({"Python"}) would return ["Python Basics"].
COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topics):
    response = []
    for course, course_topics in COURSES.items():
        if course_topics.intersection(topics):
            response.append(course)
    return response

print(covers({"Python"}))
print("-"*40)

# ---------------------
# Challenge Task 2 of 2

# Great work!

# OK, let's create something a bit more refined. 
# Create a new function named covers_all that takes a single set as an argument. 
# Return the names of all of the courses, in a list, where all of the topics in the supplied set are covered.
# 
# For example, covers_all({"conditions", "input"}) would return
# ["Python Basics", "Ruby Basics"]. 
# Java Basics and PHP Basics would be excluded because they don't include both of those topics.
def covers_all(input_set):
    response = []
    for course, topics in COURSES.items():
        if input_set.intersection(topics) == input_set:
            response.append(course)
    return response

print(covers_all({"conditions", "input"}))
