import os
import csv

print("Financial Analysis")
print("------------------------------")

# List of file
fileNumbers = ['1', '2']

# Loop through files
for numToCheck in fileNumbers:

    # Grab budget CSV file
    csvpath = os.path.join('Resources', 'budget_data_' + numToCheck + '.csv')
    print (csvpath)
    print("------------------------------")
     # Create new CSV
    newbudgetDataTXT = os.path.join('output', 'budget_data_' + numToCheck + '.txt')

    rowcount = 0

    # The list used to store all of the revenues
    Revenue = []

    # The list used to store all of the dates
    Date = []

    Total_revenue = 0
    # Reading the CSV file
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        
        next(csvreader, None)
        #  Each row is read as a row
        for row in csvreader:
            rowcount = rowcount +1
            Revenue.append(row[1])
            Date.append(row[0])

        for x in range(0,rowcount):
            Total_revenue = float(Total_revenue)+ float((Revenue[int(x)]))

        # Getting the max revenue
        Max = Revenue[0]
        Date_Max = Date[0]
        for x in range(0,rowcount):
            if(Revenue[int(x)] > Max):
                Max = Revenue[int(x)]
                Date_Max = Date[int(x)]

        # Getting the minimum revenue
        Min = Revenue[0]
        Date_Min = Date[0]
        for x in range(0,rowcount):
            if(Revenue[int(x)] < Min):
                Min = Revenue[int(x)]
                Date_Min = Date[int(x)]

    Average_revenue = "{0:.2f}".format(float(Total_revenue / rowcount))


    print("Total Month: " + str(rowcount))
    print("Total Revenue: $" + str(Total_revenue))
    print("Average Revenue: $" + str(Average_revenue))
    print("Greatest Increase: " + str(Date_Max) +" ($" + str(Max) +")")
    print("Greatest Decrease: " + str(Date_Min) +" ($" + str(Min) +")")
    print("------------------------------")

    #Writing the results of the in a text file
    with open(newbudgetDataTXT, 'w') as text_file:
        text_file.write ("Financial Analysis \n")
        text_file.write ("------------------------ \n")

        text_file.write("Total Month: " + str(rowcount) + "\n")
        text_file.write("Total Month: $" + str(Total_revenue) + "\n")
        text_file.write("Average Revenue: $" + str(Average_revenue) + "\n")
        text_file.write("Greatest Increase: " + str(Date_Max) +" ($" + str(Max) +") \n")
        text_file.write("Greatest Decrease: " + str(Date_Min) +" ($" + str(Min) +")\n")