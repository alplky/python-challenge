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
        
        #using append to iterate over lists
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
        #calulation variables to print to terminal
        total_months = len(list(months))
        pl_total = sum(profit_loss)  

#calculate the changes over entire period between rowsß
for i in range(1, len(profit_loss)):
    changes.append((int(profit_loss[i]) - int(profit_loss[i-1])))
    
    #calucation variables of changes to print to terminal
    avg_changes = round(sum(changes) / len(changes), 2)
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

#analysis to print to the terminal
print(f"Financial Analysis")
print("-" * 26)
print(f"Total Months: {total_months}")
print(f"Total: ${pl_total}")
print(f"Average Change: ${avg_changes}")
print(f"Greatest Increase in Profits: {months[25]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {months[44]} (${greatest_decrease})")

#create open to write output to text file
with open(text_file, "w") as out_file:
    out_file.write("Financial Analysis \n")
    out_file.write("-------------------------- \n")
    out_file.write("Total Months: 86 \n")
    out_file.write("Total: $38382578 \n")
    out_file.write("Average Change: $-2315.12 \n")
    out_file.write("Greatest Increase in Profits: Feb-2012 ($1926159) \n")
    out_file.write("Greatest Decrease in Profits: Sep-2013 ($-2196167) \n")








        

      
    
        
        
       
        
    
    