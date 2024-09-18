#import required modules 
import os
import csv

#path to find election_data CSV file in nested Resources folder
election_data_csv = os.path.join('Resources','election_data.csv')

#define variables 
total_votes = 0
candidates={}
winner=""
winning_votes=0

#load and read the election_data CSV file
with open(election_data_csv) as file:
    csvreader=csv.reader(file,delimiter=",")

    #skip the header row
    next(csvreader)

    #evaluate each row in the CSV file
    for row in csvreader:
        total_votes+=1

        #count the votes per candidate
        if row[2] in candidates:
             candidates[row[2]] += 1
        else:
             candidates[row[2]] = 1

    #calculate percentage of votes per candidate
    results={}

    for candidate, votes in candidates.items():
        percent=votes/total_votes
        results[candidate]=(percent, votes)

        #identify the winner
        if votes>winning_votes:
            winning_votes=votes
            winner=candidate

#print resuls of analysis        
print("Election Results")    
print("----------------")
print(f"Total Votes:{total_votes}")
print("----------------")

for candidate, (percentage,votes) in results.items():
    #print results of analysis
    print(f"{candidate}: {percentage:.3%} ({votes})")

#print results of analysis
print("----------------")
print(f"Winner: {winner}")
   
#export the results to a text display file
output_file = "Analysis/ElectionAnalysis.txt"
with open(output_file, "w") as f:
    f.write(f"Election Results\n")
    f.write(f"----------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write(f"----------------------------\n")
    for candidate, (percentage, votes) in results.items():
        f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    f.write(f"----------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"----------------------------\n")
    print(os.getcwd())