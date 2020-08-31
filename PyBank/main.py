import os 
import csv

out_path = "updated_budget_data.csv"
out_header = [
    "Date",
    "Profit/Losses",
    "Changes"
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
        
        profit_losses = int(row["Profit/Losses"])
        
        #using append to iterate over lists
        months.append(row["Date"])
        profit_loss.append(profit_losses)
        
        #Calulation variables to print to terminal
        total_months = len(list(months))
        pl_total = sum(profit_loss)
        
        #New row for change in profit/losses over each month
        row["Changes"] = profit_losses - profit_losses
        
        #Create csv with new column of changes over each month
        dict_writer.writerow(row)
        
    print(f"Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_months}")
    print(f"Total: ${pl_total}")

        

      
    
        
        
       
        
    
    