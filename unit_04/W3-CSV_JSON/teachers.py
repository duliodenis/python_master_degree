#
#  CSV and JSON in Python Workshop: Teachers
#  Python Techdegree
#
#  Created by Dulio Denis on 12/30/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  CSVs, or comma-separated value files, are a 
#  common file-based database-like format.
#  Python has a built-in `csv` module that makes
#  working with these files quick and easy.
# ------------------------------------------------
import csv

with open('teachers.csv', 'a') as csvfile:
    fieldnames = ['first_name', 'last_name', 'topic']
    teachwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    teachwriter.writeheader()
    teachwriter.writerow({
        'first_name': 'Kenneth',
        'last_name': 'Love',
        'topic': 'Python'
    })
    teachwriter.writerow({
        'first_name': 'Alena',
        'last_name': 'Holligan',
        'topic': 'PHP'
    })
