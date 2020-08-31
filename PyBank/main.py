import os 
import csv

out_path = "updated_budget_data.csv"
out_header = [
    "Date",
    "Profit/Losses",
    "Profit/Losses_2"
]

path = os.path.join("Resources", "budget_data.csv")

months = []
profit_loss = []
average_of_changes = []
greatest_increase = []
greatest_decrease = []

with open(path, "r") as in_file, open(out_path, "w+") as out_file:
    dict_reader = csv.DictReader(in_file)
    dict_writer = csv.DictWriter(out_file, out_header)
    
    dict_writer.writeheader()
    
    for row in dict_reader:
        row = dict(row)
        
        row["Profit/Losses_2"] = int(row["Profit/Losses"])
        
        dict_writer.writerow(row)
        
        profit_losses = int(row["Profit/Losses"])
        
        months.append(row["Date"])
        profit_loss.append(profit_losses)
        
        total_months = len(list(months))
        pl_total = sum(profit_loss)
        
    print(f"Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_months}")
    print(f"Total: ${pl_total}")
        

      
    
        
        
       
        
    
    