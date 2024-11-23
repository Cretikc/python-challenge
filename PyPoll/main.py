#!/usr/bin/env python
# coding: utf-8

# In[14]:


# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("./Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("./analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = set ()
vote_by_candidate = {}


# Winning Candidate and Winning Count Tracker
winner =''
winning_vote = 0


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidates.add (row [2])
        
        
        # If the candidate is not already in the candidate list, add them
        if row[2] not in vote_by_candidate:
            vote_by_candidate [row[2]]= 1
            
        # Add a vote to the candidate's count
        else:
            vote_by_candidate [row[2]]= vote_by_candidate [row[2]] + 1

print(total_votes)
print(vote_by_candidate)

#Calculate percentage vote by candidate and winner
percentage_vote_by_candidate = {}

#iterate on candiate name, vote on the dictionary vote_by_candidate
for name, vote_count in vote_by_candidate.items (): 
    percentage_vote_by_candidate [name] = round (vote_count/total_votes *100,3)
    
    #Check the winner
    if vote_count > winning_vote:
        winner = name
        winning_vote = vote_count

print(percentage_vote_by_candidate)
    

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('----------------------------\n')
    txt_file.write('Total_votes:' + str(total_votes) + '\n')
    txt_file.write ('----------------------------\n')
    for candidate, percentage in percentage_vote_by_candidate.items ():
        txt_file.write( candidate  + ': ' + str (percentage_vote_by_candidate [candidate]) + '% (' + str(vote_by_candidate[candidate]) + ')\n')
    txt_file.write ('----------------------------\n')
    txt_file.write('winner: ' + winner + '\n')
    txt_file.write ('----------------------------\n')
    

  


# In[ ]:




