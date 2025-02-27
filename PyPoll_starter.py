# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
vote_dic = {}

# Winning Candidate and Winning Count Tracker
win_can = "Place Holder"
win_vote = 0
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        can_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if can_name not in vote_dic:
            vote_dic[can_name] = [0, 0]

        # Add a vote to the candidate's count
        vote_dic[can_name][0] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    csvwriter = csv.writer(txt_file, delimiter=",")
    print(f"\nTotal votes: {total_votes}")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in vote_dic:

        # Get the vote count and calculate the percentage
        vote_perc = vote_dic[candidate][0] / total_votes

        # Update the winning candidate if this one has more votes
        if vote_dic[candidate][0] > win_vote:
            win_can = candidate
            win_vote = vote_dic[candidate][0]
        # Print and save each candidate's vote count and percentage
        vote_dic[candidate][1] = vote_perc
        print(f"{candidate} has {vote_dic[candidate][0]} votes for a percentage of {format(vote_dic[candidate][1], ".2%")}! ")

    # Generate and print the winning candidate summary
    print(f"The winning candidate is {win_can} with {vote_dic[win_can][0]} votes, winning with {format(vote_dic[win_can][1], ".2%")} of the total votes cast!")

    # Save the winning candidate summary to the text file
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------------------------"])
    csvwriter.writerow(["Total votes:" + str(total_votes)])
    csvwriter.writerow(["--------------------------------------"])
    for candidate in vote_dic:
        csvwriter.writerow([str(candidate) + ": " + str(format(vote_dic[candidate][1], ".3%")) + " (" + str(vote_dic[candidate][0]) + ")"])
    csvwriter.writerow(["--------------------------------------"])
    csvwriter.writerow(["Winner: " + str(win_can)])
    csvwriter.writerow(["--------------------------------------"])
