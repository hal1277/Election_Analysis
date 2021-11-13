# Election_Analysis

## Overview of Election Audit

The task was to use Python to help assist a Colorado board of elections employee to automate the audit the election results for a US congressional precinct in Colorado.  

The requirement included using the data to provide a total vote count, total votes per candidate, percentage of total votes per candidate, the winning candidate, the votes per county, percentage of votes per county, and the largest county by number of votes. 

## Election Audit Results

- Total Votes:
    
    Total votes cast were calculated by using Python code to count the number of rows of data.   This produced a total vote count of 369,711.

        '# For each row in the CSV file.
        for row in reader:

            # Add to the total vote count
            total_votes = total_votes + 1

- Votes per County:

    Total votes per county were calcuated by using Python code to count the number of rows of data associated with each county name.  For each time a county name was encountered for the first time the county name was added to the county list dictionary.
    
        if county_name not in county_list:
            
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        '# 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

- Percentage Votes per County:

    Percentage votes per county were calculated by using Python code to divide the number of votes per county by the total number of votes.  
    
        votes = county_votes.get(county_name)
        
        vote_percentage = float(votes) / float(total_votes) * 100

    Total votes and percentage of votes per county:

    County Votes:
    Jefferson: 10.5% (38,855)

    Denver: 82.8% (306,055)

    Arapahoe: 6.7% (24,801)

- Largest County: 

    The largest county was determined by testing for which county the following condition held true (i.e. the county where the most votes were cast)

        if (votes > county_count) and (vote_percentage > county_percentage):
             county_count = votes
             largest_county = county_name
             county_percentage = vote_percentage

    Largest County Turnout: Denver

- Votes per candidate:

    Total votes per candiate were calculated very similarily to the votes per county except rows were county based on candate name.  For each time a candidate name was encountered for the first time the candidate name was added to the candiate list dictionary. 

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        '# Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

- Percentage Votes per candidate:

    Percentage votes per candidate were calculated by dividiing the number of votes per candidate by the total number of votes. 

        for candidate_name in candidate_votes:

            # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100

    Total votes and percentage of votes per candidate:

    Charles Casper Stockham: 23.0% (85,213)

    Diana DeGette: 73.8% (272,892)

    Raymon Anthony Doane: 3.1% (11,606)

- Winning cadidate: 

    The wininng candiate and their total votes and % of total votes were tabulated by testing the following condition:

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    Winning candidate:

    Winner: Diana DeGette

    Winning Vote Count: 272,892
    
    Winning Percentage: 73.8%

## Election Audit Summary

This code provides an efficient and automated way to tabulate the election results.  It's possible to modify this code to allow it to be used for other elections.  

One possible modifiction would be if the data contained multiple levels of hierarchy such as state, congressional district, county and polling station.  Additional code could be added to the for looop to tabulate the votes and percentages at each of these levels of hierarchy.  The code can be expanded to handle larger and more complex data sets. 

Another possible modifiction would be to tabulate the vote counts by vote type if that data were present.  An election baord my be interested to see by what method each vote was cast (mail in, punch cards, direct recording electronic).  This information could be helpful for future election planning.  Again it would require some additional code within the existing for loop to tabulate based on this criteria.  In this case and the scenario above it's also necesary to define new dictionaries and libraires to define and hold the data that will be captured.  