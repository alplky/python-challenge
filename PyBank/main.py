import os 
import csv

#new csv for calulating monthly changes
out_path = "updated_budget_data.csv"
out_header = [
    "Date",
    "Profit/Losses",
    "Changes"
]

path = os.path.join("Resources", "budget_data.csv")

#empty lists to iterate over for each analysis finding
months = []
profit_loss = []
average_of_changes = []
greatest_increase = []
greatest_decrease = []


with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        #using append to iterate over lists
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
        #Calulation variables to print to terminal
        total_months = len(list(months))
        pl_total = sum(profit_loss)
    
    #analysis to print to the terminal
    print(f"Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_months}")
    print(f"Total: ${pl_total}")

        

      
    
        
        
       
        
    
    