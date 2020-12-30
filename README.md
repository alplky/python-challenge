# python-challenge

## Background

It's time to put away the Excel sheet and enter the world of programming with Python. This assignment requires using Pythons concepts to complete two separate challenges: PyBank and PyPoll. Both of challenges encompasses a real-world situation where Python scripting skills can come in handy. 

## Technologies Used

* Python

## Objectives

1. PyBank: Create a script for analyzing the financial records of a company. A set of financial data called budget_data.csv is provided for analysis. The dataset consists of two columns: date and profits/losses.

* Calculations: 
   * The total number of months included in the dataset
   * The net total amount of "Profit/Losses" over the entire period
   * The average of the changes in "Profit/Losses" over the entire period
   * The greatest increase in profits (date and amount) over the entire period
   * The greatest decrease in losses (date and amount) over the entire period

2. PyPoll: Help a small, rural town moderinze its vote counting process. Create a python script that analyzes the votes for each candidate and write out the analysis as a text file. A set of poll data is provided called election_data.csv. The dataset is composed of three columns: voter id, county, and candidate.

* Calculations: 
   * The total number of votes cast
   * A complete list of candidates who received votes
   * The percentage of votes each candidate won
   * The total number of votes each candidate won
   * The winner of the election based on popular vote

### PyBank
```Python
path = os.path.join("Resources", "budget_data.csv")

text_file = os.path.join("Analysis", "pybank_analysis.txt")

months = []
profit_loss = []
changes = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        months.append(row[0])
        profit_loss.append(int(row[1]))

for i in range(1, len(profit_loss)):
    changes.append((int(profit_loss[i]) - int(profit_loss[i-1])))

print(f"Financial Analysis")
print("-" * 26)
print(f"Total Months: {len(list(months))}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${round(sum(changes) / len(changes), 2)}")
print(f"Greatest Increase in Profits: {months[25]} (${max(changes)})")
print(f"Greatest Decrease in Profits: {months[44]} (${min(changes)})")

with open(text_file, "w") as out_file:
    out_file.writelines(["Financial Analysis \n",
                        "-------------------------- \n",
                        "Total Months: 86 \n",
                        "Total: $38382578 \n",
                        "Average Change: $-2315.12 \n",
                        "Greatest Increase in Profits: Feb-2012 ($1926159) \n",
                        "Greatest Decrease in Profits: Sep-2013 ($-2196167) \n"])
```
  
### PyPoll
```Python
path = os.path.join("Resources", "election_data.csv")

text_file = os.path.join("Analysis", "pypoll_analysis.txt" )

votes = []
candidates = []

counter = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "OTooley": 0
}

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        votes.append(row)
        candidates.append(row[2])

for candidate in candidates:
    if candidate == "Khan":
        counter["Khan"] += 1
    elif candidate == "Correy":
        counter["Correy"] += 1
    elif candidate == "Li":
        counter["Li"] += 1
    elif candidate == "O'Tooley":
        counter["OTooley"] += 1
    
    khan_votes = int(counter["Khan"])
    correy_votes = int(counter["Correy"])
    li_votes = int(counter["Li"])
    otooley_votes = int(counter["OTooley"])
    
    total_votes = khan_votes + correy_votes + li_votes + otooley_votes
    k_percent = (khan_votes / total_votes) * 100
    c_percent = (correy_votes / total_votes) * 100
    l_percent = (li_votes / total_votes) * 100
    o_percent = (otooley_votes / total_votes) * 100
    
    
print(f"Election Results")
print("-" * 25)
print(f"Total Votes: {len(votes)}")
print("-" * 25)
print(f"Khan: {round(k_percent)}% ({counter['Khan']})")
print(f"Correy: {round(c_percent)}% ({counter['Correy']})")
print(f"Li: {round(l_percent)}% ({counter['Li']})")
print(f"O'Tooley: {round(o_percent)}% ({counter['OTooley']})")
print("-" * 25)
print(f"Winner: Khan")
print("-" * 25)

with open(text_file, "w") as out_file:
    out_file.writelines(["Election Results \n", 
                         "------------------------- \n", 
                         "Total Votes: 3521001 \n", 
                         "------------------------- \n", 
                         "Khan: 63% (2218231) \n", 
                         "Correy: 20% (704200) \n", 
                         "Li: 14% (492940) \n", 
                         "O'Tooley: 3% (105630) \n", 
                         "------------------------- \n", 
                         "Winner: Khan \n", 
                         "------------------------- \n"])
```
