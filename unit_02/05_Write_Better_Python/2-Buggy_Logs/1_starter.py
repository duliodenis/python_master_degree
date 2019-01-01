#
#  Object-Oriented Python: Write Better Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/23/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: Log Messages
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Log a message with a level of DEBUG. The message can say anything you want.
import logging

logging.basicConfig(filename='cc.log', level=logging.DEBUG)

# Write your code below here
logging.debug('Anything you want.')

# ------------------------------------------------
#  Challenge Task 2 of 2
#  Log "The French have the Grail" as a WARNING level message.
logging.warning("The French have the Grail")