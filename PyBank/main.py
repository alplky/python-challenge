import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

months = []
profit_loss = []
average_of_changes = []
greatest_increase = []
greatest_decrease = []

with open(path, "r") as file:
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:
        row = dict(row)
        
        value = int(row["Profit/Losses"])
        
        months.append(row["Date"])
        profit_loss.append(value)
        
        total_months = len(list(months))
        pl_total = sum(profit_loss)
        
    print(f"Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_months}")
    print(f"Total: ${pl_total}")
    
        

      
    
        
        
       
        
    
    