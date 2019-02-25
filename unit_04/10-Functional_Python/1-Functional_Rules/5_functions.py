#
#  Functional Python: Log and Run or Return
#  Python Techdegree
#
#  Created by Dulio Denis on 2/25/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
def log_and_run(func):
    print("I just got {}".format(func.__name__))
    return func()

def log_and_return(func):
    print("I just got {}".format(func.__name__))
    return func

def say_hello():
    print('Hello!')


print('log and run:')
log_and_run(say_hello)

print('log and return:')
log_and_return(say_hello)

print('hola:')
hola = log_and_return(say_hello)
hola()
