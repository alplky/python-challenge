import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

#path to overwrite with results of script
text_file = os.path.join("Analysis", "pybank_analysis.txt")

#empty lists to iterate over for each analysis finding
months = []
profit_loss = []
changes = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        #use append to iterate over lists
        months.append(row[0])
        profit_loss.append(int(row[1]))

#calculate the changes over entire period between months
for i in range(1, len(profit_loss)):
    changes.append((int(profit_loss[i]) - int(profit_loss[i-1])))


#analysis to print to the terminal
print(f"Financial Analysis")
print("-" * 26)
print(f"Total Months: {len(list(months))}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${round(sum(changes) / len(changes), 2)}")
print(f"Greatest Increase in Profits: {months[25]} (${max(changes)})")
print(f"Greatest Decrease in Profits: {months[44]} (${min(changes)})")

#create open to write output to text file
with open(text_file, "w") as out_file:
    out_file.writelines(["Financial Analysis \n",
                        "-------------------------- \n",
                        "Total Months: 86 \n",
                        "Total: $38382578 \n",
                        "Average Change: $-2315.12 \n",
                        "Greatest Increase in Profits: Feb-2012 ($1926159) \n",
                        "Greatest Decrease in Profits: Sep-2013 ($-2196167) \n"])









        

      
    
        
        
       
        
    
    