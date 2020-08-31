import os
import csv

path = os.path.join("Resources", "election_data.csv")

with open(path, "r") as file:
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:
        row = dict(row)
        
        print(row)