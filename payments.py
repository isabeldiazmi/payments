""" 
import csv

file = open('/Users/isabeldiazmiranda/OneDrive/Jeeves/PaymentsScript/STP.csv')
csvreader = csv.reader(file)

header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
"""

import pandas as pd

data= pd.read_csv('/Users/isabeldiazmiranda/OneDrive/Jeeves/PaymentsScript/STP.csv')
print(data)