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
 #candidates=[]
 #candidatevotes=[]

    #total_vote=0

    for row in csv_reader:
        votes.append(row[0])
        #total_vote += 1
       
    #candidates and votes they got
    #Khan=int(candidates.count("Khan"))
    #Correy=int(candidates.count("Correy"))
    #Li=int(candidates.count("Li"))
    #O'Tooley=int(candidates.count("O'Tooley"))

    #% of total vote for each canidate
    #Khan_per=(Khan/total_vote)*100
    #Correy_per=(Correy/total_vote)*100
    #Li_per=(Li/total_vote)*100
    #O'Tooley_per=(O'Tooley/total_vote)*100


    print("Election Results")
    print("---------------------------")
    print("Total Votes:", sum(votes)
    #print("Khan:", khan_per Khan)
    