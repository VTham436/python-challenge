import os
import csv


pypoll_csv = os.path.join("../PyPoll/Resources/election_data.csv")

total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #header row not needed
    header = next(csv_reader)
    
    for row in csv_reader:
        total_votes +=1
        #candidate votes
        if row[2] == "Charles Casper Stockham":
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes +=1

#Winner lists for dictionary
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_votes, diana_votes, raymon_votes]

#Zipping the two lists to find winner
candidates_and_votes = dict(zip(candidates, votes))
winner = max(candidates_and_votes, key=candidates_and_votes.get)

#Percentage variables
charles_pct = (charles_votes/total_votes) * 100
diana_pct = (diana_votes/total_votes) * 100
raymon_pct = (raymon_votes/total_votes) * 100

print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total_votes}")
print(f"----------------")
print(f"Charles Casper Stockham: {charles_pct:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_pct:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_pct:.3f}% ({raymon_votes})")
print(f"----------------")
print(f"Winner: {winner}")

#Export text file
output_file = ("../PyPoll/Analysis.txt")

with open(output_file,"w") as file:
    
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------\n")
    file.write(f"Charles Casper Stockham: {charles_pct:.3f}% ({charles_votes})\n")
    file.write(f"Diana DeGette: {diana_pct:.3f}% ({diana_votes})\n")
    file.write(f"Raymon Anthony Doane: {raymon_pct:.3f}% ({raymon_votes})\n")
    file.write(f"----------------\n")
    file.write(f"Winner: {winner}")