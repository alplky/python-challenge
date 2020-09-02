import os
import csv

path = os.path.join("Resources", "election_data.csv")

#empty lists to append
votes = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        #appending to print calculations
        votes.append(row)

print(f"Election Results")
print("-" * 25)
print(F"Total Votes: {len(votes)}")
print("-" * 25)