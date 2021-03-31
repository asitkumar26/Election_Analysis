import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')


# Assign a variable to save the file to a path.
file_to_save =  os.path.join('Analysis','election_analysis.txt') 

# 1. Initialize a total vote counter.
total_votes = 0

candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    for row in file_reader:
      total_votes += 1
            
        #print(row)
        
        
      candidate_name = row[2]
      if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        candidate_votes [candidate_name] = 0

      candidate_votes [candidate_name] += 1
      
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list  
    for candidate_name in candidate_votes:
      # Retrieve vote count of a candidate.
      votes = candidate_votes[candidate_name]

      # Calculate the percentage of votes.
      vote_percentage = float(votes) / float(total_votes) * 100

      #  To do: print out each candidate's name, vote count, and percentage of
      # votes to the terminal.

      # Determine winning vote count and candidate
      # Determine if the votes is greater than the winning count.
      if votes > winning_count:
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.
      #print(f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.")
      print(f"{candidate_name}: {round(vote_percentage,1)}% ({votes})")
      
       
       
       

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
        
#print(total_votes)
#print(candidate_votes)
    # Read and print the header row.
  #  header = next(file_reader)
  #  print(header)


#with open(file_to_save,'w') as txt_file:
#    txt_file.write ("Countries in the Election\n----------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")


#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes.
#3. The percentage of votes each candidate won
#4. The total nuber of votes each candidate won
#5. The winner of the election based on popular bote.