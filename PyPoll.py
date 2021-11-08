# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:59:49 2021

@author: zionh
"""
# The data we need to retrieve
# 1. The total number of votes
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


import csv
#dir(csv)
import os
import random
#dir(random)
import numpy
#dir (numpy)

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        # Add the total vote count
        total_votes += 1
    
        # Get the candidate name from each row
        candidate_name = row[2]
        
        # if the candidate dose not match any existing candidate add it to the 
        # candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #2. And begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
#using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
        
    #Print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results, end="")
    # 4. Print the candidate name and percentage votes.
        
    txt_file.write(election_results)
    
    
    
    # Determine the percentage of votes for each candidate by looping through the counts
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        
        
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")   
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
       
        #Determine winning vote count and candidate
        # 1. Detimine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. if true then set winning_count = votes and winning_percent = 
            # vote_percentage
                    
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
            
            
            
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # SAve the winning cadidates' name to the text file.
    txt_file.write(winning_candidate_summary)
                
 
                




   
    
    
   
    
    










