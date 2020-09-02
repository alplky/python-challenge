import os
import csv

path = os.path.join("Resources", "election_data.csv")

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

#adds 1 vote for each candidates name found in candidates 
for candidate in candidates:
    if candidate == "Khan":
        counter["Khan"] += 1
    elif candidate == "Correy":
        counter["Correy"] += 1
    elif candidate == "Li":
        counter["Li"] += 1
    elif candidate == "O'Tooley":
        counter["OTooley"] += 1
    
print(f"Election Results")
print("-" * 25)
print(f"Total Votes: {len(votes)}")
print("-" * 25)
print(f"Khan: ({counter['Khan']})")
print(f"Correy: ({counter['Correy']})")
print(f"Li: ({counter['Li']})")
print(f"O'Tooley: ({counter['OTooley']})")