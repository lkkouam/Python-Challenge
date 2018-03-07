# Part 1
import os
import csv
import collections

print ("Election Results")
print ("------------------------")
# List of file
fileNumbers = ['1', '2']

# Loop through files
for numToCheck in fileNumbers:

    # Grab wrestling CSV
    electionDataCSV = os.path.join('Resources', 'election_data_' + numToCheck + '.csv')

    # Create new CSV
    newelectionDataCSV = os.path.join('output', 'election_data_' + numToCheck + '.csv')

    # Set empty list variables
    voterID = []
    county = []
    candidate = []

    TotalVotes = 0
    CountVote = 0
    # Open current wrestling CSV
    with open(electionDataCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')
        # File name
        print (str(electionDataCSV))

        # Skip headers
        next(csvReader, None)
        
        for row in csvReader:

            # Append data from the row
            voterID.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
            TotalVotes = TotalVotes +1

print ("Total Votes :" + str(TotalVotes))
print ("------------------------")

#Get the unique value from the column Candidate
myset = set(candidate)
print ("List of candidates who participitated: " + str(list(myset)))


#Count the number of votes per candidate
def count_elements(candidate):
    elements ={}
    for elem in candidate:
        if elem in elements.keys():
            elements[elem] +=1
        else:
            elements[elem] =1
    return elements

#Display the name of each candidate and their results
elements = count_elements(candidate)  
for key, value in elements.items():
    #print( key + ": " + str(round((value / TotalVotes),2)*100) + "% " + "(" + str(value) + ")")
    print( key + ": " + "{0:.2f}".format((value / TotalVotes)*100) + "% " + "(" + str(value) + ")")

#Display the name of the winner
elements = count_elements(candidate) 
max_value = max(elements.values())  # maximum value
max_keys = [k for k, v in elements.items() if v == max_value] # getting all keys containing the `maximum`
#print(max_value, max_keys)
print("The winner is" + " " + str(max_keys) + " with " + str(max_value) + " votes.")
