import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')


# Assign a variable to save the file to a path.
file_to_save =  os.path.join('Analysis','election_analysis.txt') 


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    for row in file_reader:
        print(row[0])


    # Read and print the header row.
    header = next(file_reader)
    print(header)


#with open(file_to_save,'w') as txt_file:
#    txt_file.write ("Countries in the Election\n----------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")


#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes.
#3. The percentage of votes each candidate won
#4. The total nuber of votes each candidate won
#5. The winner of the election based on popular bote.