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

       
    #candidates and votes
    Khan=int(candidates.count("Khan"))
    Correy=int(candidates.count("Correy"))
    Li=int(candidates.count("Li"))
    OTooley=int(candidates.count("O'Tooley"))

    #% of total vote for each canidate
    allvotes=(len(votes))
    
    Khan_per=round(int(Khan)/(allvotes),3)
    Correy_per=round(int(Correy)/(allvotes),3)
    Li_per=round(int(Li)/(allvotes),3)
    OTooley_per=round(int(OTooley)/(allvotes),3)


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
print(f'Khanp: {Khan_per:.3%}, ({Khan})')
print(f'Correy: {Correy_per:.3%}, ({Correy})')
print(f'Li: {Li_per:.3%}, ({Li})')
print(f'O Tooley: {OTooley_per:.3%}, ({OTooley})')
print("Winner:", (Winner))

    