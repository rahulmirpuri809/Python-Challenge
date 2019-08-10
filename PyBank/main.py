import os
import csv


pbfiles = os.path.join('Pybank','Resources','budget_data.csv')
# create variables for the information we need such as totalm months, 
# total revenue, a previous revenue that we will continuously reset 
# in our following for loop to reference when we calculate revenue changes
# then we add those revenue changes to a list to find the greatest increase and decrease

count_by_months = 0
totalrevenue = 0
previousrevenue = 0
revenuechanges = []
greatestincrease = 0
greatestdecrease = 0
greatestmonth = ""
lowestmonth = ""
with open (pbfiles, newline = '') as csvfile:
    csvpath = csv.reader(csvfile, delimiter = ',')
    header = next(csvpath)
    
    
    for row in csvpath:
        # split the first cell into month and date 
        # skips header, adds one to months count for each month in the csv

        month = row[0].split("-")[0]
        if month == "Date":
            continue
        else:
            count_by_months = count_by_months + 1
        if row[1] == "Profit/Losses":
            continue
        else: 
        # adds the current revenue to our variable existing outside the for loop to keep track of totals
        # calculates revenue change and resets previous revenue to the current revenue for the next iteration
        # adds revenue change into the list and sets the greatest increase /decrease for upcoming iterations to compare to 
            totalrevenue = totalrevenue + int(row[1])
            revenuechange = int(row[1]) - previousrevenue
            previousrevenue = int(row[1])
            revenuechanges = revenuechanges + [revenuechange]
            if int(row[1]) > greatestincrease:
                greatestincrease = int(row[1])
                greatestmonth = row[0]
            if int(row[1]) < greatestdecrease:
                greatestdecrease = int (row[1])
                lowestmonth = row[0]

    # calculate average by summing total changes in revenue by how many changes there were            
    averagechange = int(sum(revenuechanges)/len(revenuechanges))

    print(f"Financial Analysis")
    print(f"----------------------")
    print(f"Total: ",totalrevenue)
    print(f"Average Change: ",averagechange)
    print(f"Greatest Increase in Profits: ",greatestmonth, (greatestincrease))
    print(f"Greatest Decrease in Profits: ",lowestmonth, (greatestdecrease))

    PyBank_Output = os.path.join('PyBank','Resources','PyBank_Budget_Results.text')
    with open (PyBank_Output, 'w') as txtfile:
        txtfile.write(f"Financial Analysis \n")
        txtfile.write(f"---------------------- \n")
        txtfile.write(f"Total: {totalrevenue} \n" )
        txtfile.write(f"Average Change: {averagechange} \n")
        txtfile.write(f"Greatest Increase in Profits: {greatestmonth} ({(greatestincrease)}) \n")
        txtfile.write(f"Greatest Decrease in Profits: {lowestmonth} ({greatestdecrease}) \n)