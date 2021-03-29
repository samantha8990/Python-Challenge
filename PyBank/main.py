import os
import csv

#get file path
pybank_path= os.path.join('PyBank','Resources','pybank.csv')

#open file
with open(pybank_path) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    csv_reader=next(csv_file)

#set variables
    months=[]
    profit=[]
    #maxprofit=[]
    #minprofit=[]

    for row in csv_reader:
        months.append(row[0])
        profit.append(int(row[1]))

        #if



    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:", len(months))
    print("Total:", sum(profit))
       
  

