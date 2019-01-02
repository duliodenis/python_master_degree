#
#  CSV and JSON in Python Workshop: Artifacts
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

print("> --------- reader ------------")
with open("museum.csv", newline = "") as csvfile:
    artreader = csv.reader(csvfile, delimiter="|")
    rows = list(artreader)
    for row in rows[:2]:
        print(', '.join(row))

print("> --------- DictReader ------------")
with open("museum.csv", newline = "") as csvfile:
    artreader = csv.DictReader(csvfile, delimiter="|")
    rows = list(artreader)
    for row in rows[1:3]:
        print(row['group1'])
