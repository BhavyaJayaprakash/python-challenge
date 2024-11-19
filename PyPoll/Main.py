#Import os module 
import os
#Import csv module
import csv 

# Files to load and output (update with correct file paths)
csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)


# Declare and Initialize variables for total votes cast in dataset, votes cast for each candidate in dataset
total_votes = []

# Define lists and dictionaries to track candidate names and vote counts
stockham_votes = 0
degette_votes = 0
doane_votes = 0

# Open the CSV file and process it
with open(csvpath,encoding="utf-8") as csvfile:

    # Read with comma delimited 
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    
    # Skip the header row
    csv_header = next(csvreader)

    # Loop through each row of the dataset and process it
    for row in csvreader:
        # Count number of votes in dataset
        total_votes.append(row[0])
        
        # Count votes for each candidate
        if row[2] == "Charles Casper Stockham":
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane_votes +=1

# Make dictionaries out of lists to find winner
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham_votes, degette_votes, doane_votes]

# Zip to pair candidates with corresponding votes and obtain the max to determine winner
votes_dict = dict(zip(candidates, candidate_votes))
winner = max(votes_dict, key=votes_dict.get)

# Declare variable for total_votes as an integer for calculations
total_vote_count = len(total_votes)

# Calculate percentages of votes for each candidate
stockham_percent = (stockham_votes/total_vote_count) * 100
degette_percent = (degette_votes/total_vote_count) * 100
doane_percent = (doane_votes/total_vote_count) * 100

# Formatting Printing Election Results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes : {len(total_votes)}" )
print("-------------------------")

# Printing percentages of votes for each candidate, rounded to 3 decimal points, and print number of votes per candidate
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
analysis = os.path.join("Analysis", "Election_Analysis.txt")
with open(analysis,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes : {len(total_votes)}" )
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")
