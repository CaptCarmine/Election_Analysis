print("Hello world")

counties = ['Arapahoe', 'Denver', 'Jefferson']
if counties[1] == 'Denver':
    print(counties[1])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key1, key2 in counties_dict.items():
    print(f'{key1} county has {key2:,} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for dict in voting_data:
    print(f'{dict["county"]} count has {dict["registered_voters"]:,} registered voters.')    


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)    