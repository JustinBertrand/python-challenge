import os
import csv

read_path = os.path.join("PyPoll", "Resources", "election_data.csv")
write_path = os.path.join("PyPoll", "output.txt")
vote_stats = {} #establish dictionary to hold dictionaries of candidate stats
total_votes = 0
most_votes = 0
winner = ""

with open (read_path, newline = "", encoding = "utf8") as temp_file:
    election_data = csv.reader(temp_file, delimiter = ",")
    
    #read the header row first (skip if there is no header)
    data_header = next(temp_file)

    for row in election_data: #tally votes and add new candidates to dictionary
        candidate = row[2]
        if candidate not in vote_stats: ###votes_per:
            vote_stats[candidate] = {}
            vote_stats[candidate]["Votes"] = 1
            #establish new entry for key ***candidate*** with value = 1
        else:
            vote_stats[candidate]["Votes"] += 1
            #add one to value of ***candidate*** in dictionary
        total_votes += 1

candidates = list(vote_stats.keys()) #establishes list of candidate names from master dictionary

for candidate in candidates:
    vote_stats[candidate]["Percent"] = round((vote_stats[candidate]["Votes"]/total_votes)*100, 0)
    #adds name: percent pair to dictionary for each candidate
    if vote_stats[candidate]["Votes"] > most_votes: #if candidate has most votes:
        most_votes = vote_stats[candidate]["Votes"] #update highest vote count
        winner = candidate                          #declare candidate as winner

readout = (f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n")
#create string to display results
for candidate in vote_stats: #append each candidates results to display string
    readout = readout + (candidate + ": " + str(vote_stats[candidate]["Percent"]) + "% (" + (str(vote_stats[candidate]["Votes"])) + ")\n")
readout = readout + (f"-------------------------\nWinner: {winner}") #add winner to string
print(readout)

# Specify the file to write to
write_path = os.path.join("PyPoll", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(write_path, "w") as output_file:
    output_file.write(readout) #print results to txt file