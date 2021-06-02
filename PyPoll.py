# modules imported
import os
import csv

# variables
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# candidates 
candidate_options = []
candidate_votes = {}
#winning Candidate and tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# 1. Open the data file.
with open(file_to_load) as election_data:
     # To do: perform analysis.
    file_reader = csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for column in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        candidate_name = column[2]
        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

    if votes > winning_count:    
        winning_candidate = candidate_name 
        winning_count = votes
        winning_percentage = vote_percentage
    

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,}) of the vote.\n")
# 3. Print the total votes, and candidate Options
#print(f'{total_votes:,}')
#print(f'{winning_candidate} is the winner, she had {winning_count:,} ({winning_percentage:.2f}%) total votes.')

candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
#    )
winning_candidate_summary = (
    f"---------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------\n")

 
#print(winning_candidate_summary)
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    election_results= (
    f'Election Results \n'
    f'---------------------\n'
    f'{total_votes:,}\n'
    f'---------------------\n')
    print(election_results)
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
        if votes > winning_count:    
            winning_candidate = candidate_name 
            winning_count = votes
            winning_percentage = vote_percentage
        print(candidate_results)
        txt_file.write(candidate_results)
    
    winning_candidate_summary = (
    f"---------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
# 2. Write down the names of     all the candidates.

# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.