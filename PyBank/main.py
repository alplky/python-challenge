import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

#empty lists to iterate over for each analysis finding
months = []
profit_loss = []
prof_loss = []
prof_loss_2 = []
augmtd_prof_loss = []
greatest_increase = []
greatest_decrease = []


with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        #lists for calculating changes between months
        prof_loss.append(int(row[1]))
        prof_loss_2.append(int(row[1]))
        del prof_loss[0]
        del prof_loss_2[-1]
        
        #zipping list together to calculate the difference/change between tuples
        zipped = zip(prof_loss, prof_loss_2)
        zip_prof_loss = list(zipped)
        
        #calculating the difference/change between tuples
        changes = [b - a for a, b in zip_prof_loss]
        
        #using append to iterate over lists
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
        #Calulation variables to print to terminal
        total_months = len(list(months))
        pl_total = sum(profit_loss)
    
    #analysis to print to the terminal
    print("-" * 25)
    print(f"Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_months}")
    print(f"Total: ${pl_total}")


        

      
    
        
        
       
        
    
    