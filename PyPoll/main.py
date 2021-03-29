import os
import csv

#get file path
pybank_path= os.path.join('PyPoll','Resources','pypoll.csv')

#open file
with open(pybank_path) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    csv_reader=next(csv_file)

#set variables
 votes= []
 candidates=[]
 candidatevotes=[]

 totalvote=0

    for row in csv_reader:
        votes.appen(row[2])
totalvote=len(votes)



    print("Election Results")
    print("---------------------------")
    print("Total Votes:", len(votes))
    print("Total:", sum(profit))