import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

total_months = (0)

with open(path, "r") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        row = dict(row)
        
        total_months += 1
        print(total_months)
        
        
        
    
    