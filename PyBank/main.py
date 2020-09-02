import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

#empty lists to iterate over for each analysis finding
months = []
profit_loss = []
changes = []
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
        
for i in range(1, len(csv_reader)):
#     last_period_row = csv_reader[i - 1]
#     current_period_row = csv_reader[i]
        
    changes.append()
    
#analysis to print to the terminal
print("-" * 25)
print(f"Financial Analysis")
print("-" * 25)
print(f"Total Months: {total_months}")
print(f"Total: ${pl_total}")
print(f"Average Change: ${}")
print(f"Greatest Increase in Profits: {} ${}")
print(f"Greatest Increase in Profits: {} ${}")




        

      
    
        
        
       
        
    
    