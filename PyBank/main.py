import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as file:
    csv_reader = csv.DictReader(file)
    
    total_months = len(list(csv_reader))
    
    for row in csv_reader:
        row = dict(row)
        
    print(f"Total Months: {total_months}")
        
        
       
        
    
    