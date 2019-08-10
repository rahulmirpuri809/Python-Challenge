import os
import csv

ppfiles = os.path.join('PyPoll','Resources','election_data.csv')
#set variables for total votes, votes for each candidate, and a blank list which we will fill with candidate names
votes_total = 0
khanvotes= 0
correyvotes=0
livotes=0
otooley = 0
candidates = []

with open (ppfiles, newline = '') as csvfile:
    cvsread = csv.reader(csvfile, delimiter = ',')
    header = next(cvsread)
    for row in cvsread:
    
     # for each iteration, add one to total votes, add votes to rightful candidate, add candidate name to list if not there already
        votes_total = votes_total + 1

        if row[2] == "Khan":
            khanvotes = khanvotes + 1
        elif row[2] == "Correy":
            correyvotes = correyvotes + 1
        elif row[2] == "Li":
            livotes = livotes + 1
        else:
            otooley = otooley + 1
        if row[2] in candidates:
            continue
        else:
            candidates.append(row[2])

    #find percent of each candidate by taking their individual total and dividing by the total amount of votes
    khanpercent = "{:.2%}".format(khanvotes/votes_total)
    correypercent = "{:.2%}".format(correyvotes/votes_total)
    lipercent = "{:.2%}".format(livotes/votes_total)
    otooleypercent= "{:.2%}".format(otooley/votes_total)
   
 # find which candidate had the max votes by taking the max and matching it with the winner's name
    maxwins = max([khanvotes,correyvotes,livotes,otooley])
    if maxwins == khanvotes:
        winner = "Khan"
    elif maxwins == correyvotes:
        winner = "Correy"
    elif maxwins == livotes:
        winner = "Li"
    else:
        winner = "O'Tooley"
        
    
    print(f"Election Results")
    print(f"--------------------------")
    print(f"Total Votes: {votes_total}")
    print(f"--------------------------")
    print(f"Khan: {khanpercent} ({khanvotes})")
    print(f"Correy: {correypercent} ({correyvotes})")
    print(f"Li:  {lipercent} ({livotes})")
    print(f"O'Tooley: {otooleypercent} ({otooley})")
    print(f"--------------------------")
    print(f"Winner: {winner} ({maxwins})")


    PyPoll_Output = os.path.join('PyPoll','Resources','PyPoll_Election_Results.text')
    with open (PyPoll_Output, 'w') as txtfile:

        txtfile.write(f"Election Results \n")
        txtfile.write(f"-------------------------- \n")
        txtfile.write(f"Total Votes: {votes_total} \n")
        txtfile.write(f"-------------------------- \n")
        txtfile.write(f"Khan: {khanpercent} ({khanvotes}) \n")
        txtfile.write(f"Correy: {correypercent} ({correyvotes}) \n")
        txtfile.write(f"Li:  {lipercent} ({livotes}) \n")
        txtfile.write(f"O'Tooley: {otooleypercent} ({otooley}) \n")
        txtfile.write(f"-------------------------- \n")
        txtfile.write(f"Winner: {winner} ({maxwins}) \n")