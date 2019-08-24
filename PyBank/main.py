# Import Dependencies
import os 
import csv 



# Declare CSV Path
pbfiles = os.path.join('Resources','budget_data.csv')

# Declare variables for months count, total revenue, previous revenue, a list for the revenue changes, and greatest/lost month
count_by_months = 0
totalrevenue = 0
previousrevenue = 0
revenuechanges = []
greatestincrease = 0
greatestdecrease = 0
greatestmonth = ""
lowestmonth = ""

# Open CSV and skip header 
with open (pbfiles, newline = '') as csvfile:
    csvpath = csv.reader(csvfile, delimiter = ',')
    header = next(csvpath)
    
# Iterate through csv file 
    for row in csvpath:

# Add month's revenue to total revenue
        totalrevenue = totalrevenue + (int(row[1]))

# Amend the revenue change to account for revenue change relative to previous month
        revenuechange = int(row[1]) - previousrevenue

# Reset previous revenue to the current revenue
        previousrevenue = int(row[1])

# Append revenuechanges with revenue change
        revenuechanges = revenuechanges + [revenuechange]
    
# IF statements to find value and month of greatest revenue increase and decrease 
        if revenuechange > greatestincrease:
            greatestincrease = revenuechange
            greatestmonth = row[0]
        if revenuechange < greatestdecrease:
            greatestdecrease = revenuechange
            lowestmonth = row[0]

# Have revenuechanges list start at index 1 to skip revenue at month 1           
    revenuechanges = revenuechanges[1:]

# Calculate average by summing the list of revenue changes and dividing by length of the list
    averagechange = round(sum(revenuechanges)/len(revenuechanges),2)

# Print Results
print(f"Financial Analysis")
print(f"----------------------")
print(f"Total: " "$"+str(totalrevenue))
print(f"Average Change: ","$"+str(averagechange))
print(f"Greatest Increase in Profits: ",(greatestmonth),"$"+str(greatestincrease))
print(f"Greatest Decrease in Profits: ",(lowestmonth),"$"+str(greatestdecrease))


# Write Output File
PyBank_Output = os.path.join('Resources','PyBank_Budget_Results.text')
with open (PyBank_Output, 'w') as txtfile:
    txtfile.write(f"Financial Analysis \n")
    txtfile.write(f"---------------------- \n")
    txtfile.write(f"Total: ${totalrevenue}\n")
    txtfile.write(f"Average Change: ${averagechange} \n")
    txtfile.write(f"Greatest Increase in Profits: {greatestmonth} (${(greatestincrease)}) \n")
    txtfile.write(f"Greatest Decrease in Profits: {lowestmonth} (${greatestdecrease}) \n")