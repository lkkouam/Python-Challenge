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

    # Grab election data CSV
    electionDataCSV = os.path.join('Resources', 'election_data_' + numToCheck + '.csv')
    print(electionDataCSV)
    print("------------------------------")
    # Create new CSV
    newelectionDataTXT = os.path.join('output', 'election_data_' + numToCheck + '.txt')

    # Set empty list variables
    voterID = []
    county = []
    candidate = []

    TotalVotes = 0

    # Open current election data CSV
    with open(electionDataCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
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
    print ("------------------------")
    print("The winner is" + " " + str(max_keys) + " with " + str(max_value) + " votes.")
    print("------------------------------")


    #Writing the results of the in a text file
    with open(newelectionDataTXT, 'w') as text_file:
        text_file.write ("Election Results \n")
        text_file.write ("------------------------ \n")

        text_file.write ("List of candidates who participitated: " + str(list(myset)) + "\n")
        text_file.write ("Total Votes :" + str(TotalVotes) + "\n")
        text_file.write ("------------------------ \n")

        
        elements = count_elements(candidate)  
        for key, value in elements.items():
        #print( key + ": " + str(round((value / TotalVotes),2)*100) + "% " + "(" + str(value) + ")")
            text_file.write( key + ": " + "{0:.2f}".format((value / TotalVotes)*100) + "% " + "(" + str(value) + ")\n")
    
        elements = count_elements(candidate) 
        max_value = max(elements.values())  # maximum value
        max_keys = [k for k, v in elements.items() if v == max_value] # getting all keys containing the `maximum`
        
        text_file.write ("------------------------ \n")
        text_file.write("The winner is" + " " + str(max_keys) + " with " + str(max_value) + " votes. \n")