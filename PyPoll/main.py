import os

import csv
# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')
output = '''Election Results
-------------------------
Total Votes: '''
'''369711
 -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
 -------------------------
  Winner: Diana DeGette
  -------------------------
  '''
 
with open(csvpath, encoding= 'utf') as csvfile:
     #Initialising reader to read csvfile                   
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #Skipping the first row (header)
    next(csvreader)
    
    total_votes = []
    candidates_votes = ()

# The total number of votes 

    for line in csvreader:
        total_votes.append(line[2])
total_count = len(total_votes)
output = output + str(total_count) + "\n" + "-------------------------" + "\n"
candidates = list(set(total_votes))
votes_per_candidate = []
percentage = []

# Votes per candidate
# List of candidates
for candidate in candidates:
    votes_per_candidate.append(total_votes.count(candidate))

# Percentage of votes each candidate got
for i in range (len(candidates)):
    percentage = votes_per_candidate[i]/total_count*100
    output = output + f'{candidates[i]}: {round(percentage,3)}% ({votes_per_candidate[i]}) \n'
# The winner of the vote
index_of_winner = votes_per_candidate.index(max(votes_per_candidate))
output = output + f"-------------------------\nWinner: {candidates[index_of_winner]}\n-------------------------"   


# Export result to text file and print on terminal
print(output)
csvpath = os.path.join('Analysis', 'Polling_Analysis.txt')
with open(csvpath,'w') as textfile:
    textfile.write(output)