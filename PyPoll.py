# modules imported
import os
import csv

#variables
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# 1. Open the data file.
with open(file_to_load) as election_data:

     # To do: perform analysis.
     file_reader = csv.reader(election_data)
         # Read and print the header row.
     headers = next(file_reader)
     print(headers)
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
     txt_file.write(f'Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson')
# 2. Write down the names of all the candidates.

# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.