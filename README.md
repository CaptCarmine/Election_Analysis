# Overview of the Election Audit
<!-- Explain the purpose of this analysis. -->
We were tasked with helping the Colorado Board of Elections team, with automating the process to analyze/audit the congressional election for one district in colorado. They have always used excel for this process, but have tasked us to create a Python script/program which complete a number of functions.

- This program will do the following:

  1. Tabulate the number of votes cast total.
  2. Determine the number and percent of votes cast for each county.
  3. Find the county with the largest turnout.
  4. find number and percent of votes cast for each candidate.
  5. Declare the winner of the Election for the congressional district, specifically labeling the number and percent of the votes.

## Election-Audit Results
<!--Using a bulleted list, address the following election outcomes.  -->
From our program we were able to gather the reslts to the CBOE specifications. See below for the breakdown and a screenshot of the results.

1. How many votes where cast in this congressional election?
   - There were a total of 369,711 results.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
   - Denver county had 82.8% (306,055) of the total vote.
   - Jefferson county had 10.5% (38,855) of the total vote.
   - Arapahoe county had 6.7% (24,801) of the total vote.
3. Which county had the largest number of votes?
   - Denver county had an overwhelming majority of the votes at 82.8% (306,055).
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
   - Diana DeGette had the majority of the votes at 73.8% (272,892).
   - Charles Casper Stockham came in second at 23.0% (85,213) of the Vote.
   - Raymon Anthony Doane came in last, with only 3.1% (11,606) of the Vote.
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   - Diana DeGette was the winner of this congressional district.
   - Diana accumulated 272,892 votes.
   - Her owerwhelming number of votes lead to her having 73.8% of the total vote.

![Election Results](https://github.com/CaptCarmine/Election_Analysis/blob/main/Resources/Election_analysis.png?raw=true)

## Election-Audit Summary
<!--with two examples provide a business proposal to the election commission on how this script can be used—with some modifications—for any election.-->
This script/program is a powerful tool to be able to not only easily analysis/audit the district in which Diana won, but you can with some slight modifications get the same output for any county. To do this you will need to make modifications to at least two sections of the code.

The first section of the code you will need to modify is files used for the following elections, you will need to have a different CSV, which will provide the data for the other districts. As wells a different file to export the results.

- ```Python
  #The section to determine the files to pull from and write too
  file_to_load = os.path.join("Resources", "election_results.csv")
  file_to_save = os.path.join("analysis", "election_analysis.txt")
  ```

The second section of the code you will most likely need to modify is which colmns from each row you will need. As each different district could possibly collect voting data differently you will need to verify the csv you recieve has the county, candidate in the third column, or modify it in the script.

- ```Python
  #The section which determines the colums to use
  candidate_name = row[2]
  county_name = row[1]
   ```
