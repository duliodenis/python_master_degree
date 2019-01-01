#
#  Teacher Stats Challenge
#  Python Techdegree
#
#  Created by Dulio Denis on 12/9/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  This challenge has several steps so take your time, read the instructions carefully, 
#  and feel free to experiment in Workspaces or on your own computer.
#
#  Challenge Task 1 of 5
#  For this first task, create a function named num_teachers that takes a single argument, 
#  which will be a dictionary of Treehouse teachers and their courses.
#  The num_teachers function should return an integer for how many teachers are in the dict.
def num_teachers(courses_dict):
   teachers = 0
   for teacher in courses_dict:
       teachers += 1
   return teachers

courses_dict = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}

courses_dict_2 = {'Andrew Chalkley': ['jQuery Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}

print(num_teachers(courses_dict))
print("-----------------------------")

# Challenge Task 2 of 5
# Create a new function named num_courses that will
# receive the same dictionary as its only argument.
# The function should return the total number of courses for all of the teachers.
def num_courses(courses_dict):
   courses_for_all_teachers = 0
   for item in courses_dict.values():
       courses_for_all_teachers += len(item)
   return courses_for_all_teachers

print(num_courses(courses_dict))
print("-----------------------------")

# Challenge Task 3 of 5
# Make another new function named courses that will, again,
# take the dictionary of teachers and courses.
# courses, though, should return a single list of all of the available courses
# in the dictionary. No teachers, just course names!
def courses(courses_dict):
   available_courses = []
   for course_names in courses_dict.values():
       for course_name in course_names:
           available_courses.append(course_name)
   return available_courses

print(courses(courses_dict))
print("-----------------------------")

# Challenge Task 4 of 5
# Create a function named most_courses that takes our good ol' teacher dictionary.
# most_courses should return the name of the teacher with the most courses. 
# You might need to hold onto some sort of max count variable.
def most_courses(courses_dict_2):
    most_courses = 0
    most_courses_teacher = ""

    for teacher in courses_dict_2.keys():
        if len(courses_dict_2[teacher]) > most_courses:
            most_courses_teacher = teacher 
    return most_courses_teacher

print(most_courses(courses_dict_2))
print("-----------------------------")

# Challenge Task 5 of 5
# It's official: you're awesome at Python dictionaries! 
# One last task and then you can take a well-deserved break!
# In this last challenge, I want you to create a function named stats 
# and it'll take our teacher dictionary as its only argument.
# stats should return a list of lists where the first item in each inner list 
# is the teacher's name and the second item is the number of courses that teacher has. 
# For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]
def stats(courses_dict_2):
    response = []
    for teacher, courses in courses_dict_2.items():
        response.append([teacher, len(courses)])
    return response

print(stats(courses_dict_2))
