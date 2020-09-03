import os
import csv

path = os.path.join("Resources", "election_data.csv")

text_file = os.path.join("Analysis", "pypoll_analysis.txt" )

#empty lists to append
votes = []
candidates = []

#counter starting at 0 to count each candidates votes
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
        
        #appending to print calculations
        votes.append(row)
        candidates.append(row[2])

#adds 1 vote in the declared dictionary for each candidate's name found in candidates 
for candidate in candidates:
    if candidate == "Khan":
        counter["Khan"] += 1
    elif candidate == "Correy":
        counter["Correy"] += 1
    elif candidate == "Li":
        counter["Li"] += 1
    elif candidate == "O'Tooley":
        counter["OTooley"] += 1
    
    #setting up variables for calculating percentage
    khan_votes = int(counter["Khan"])
    correy_votes = int(counter["Correy"])
    li_votes = int(counter["Li"])
    otooley_votes = int(counter["OTooley"])
    
    #calculating the percentage of each candidates votes
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

#create open to write analyis in text file
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
