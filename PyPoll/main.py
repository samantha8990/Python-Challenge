import os
import csv

#get file path
pybank_path= os.path.join('PyPoll','Resources','pypoll.csv')

#open file
with open(pybank_path) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    header=next(csv_file)

#set variables
    votes= []
    candidates=[]
  
    for row in csv_reader:
        votes.append(row[0])
        candidates.append(row[2])



       
    #candidates and votes they got
    Khan=int(candidates.count("Khan"))
    Correy=int(candidates.count("Correy"))
    Li=int(candidates.count("Li"))
    OTooley=int(candidates.count("O'Tooley"))

    #% of total vote for each canidate
    allvotes=(len(votes))
    Khan_per=(Khan/allvotes)*100
    Correy_per=(Correy/allvotes)*100
    Li_per=(Li/allvotes)*100
    OTooley_per=(OTooley/allvotes)*100


    #find winner
    if Khan > Correy > Li > OTooley:
        Winner="Khan"
    elif Correy > Khan > Li > OTooley:
        Winner= "Correy"
    elif Li > Khan > Correy > OTooley:
        Winner="Li"
    elif OTooley > Khan > Correy > Li:
        Winner="O'Tooley"

print("Election Results")
print("---------------------------")
print("Total Votes:", len(votes))
print("Khan:", (Khan_per), (Khan))
print("Correy:", (Correy_per), (Correy))
print("Li:", (Li_per), (Li))
print("O' Tooley:", (OTooley_per), (OTooley))
print("Winner:", (Winner))

    