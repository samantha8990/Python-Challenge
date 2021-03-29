import os
import csv
import statistics

#get file path
pybank_path= os.path.join('PyBank','Resources','pybank.csv')

#open file
with open(pybank_path) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    csv_reader=next(csv_file)

#set variables
    months=[]
    profit=[]
    #max_profit=[]
    #min_profit=[]
    #value_sum=0
    for row in csv_reader:
        months.append(row[0])
        #profit.append(int(row[1]))-this add all of column profit/losses
        #value_sum += int(row[1])- this add all of column profit/losses

        #calculate max profit
        #if



    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:", len(months))
    print("Total:", sum(profit))
    #print("Average Change:",) can use statistics.mean?
    #print("Greatest Increase in Profits:")
    #print("Greatest Decrease in Profits:")

       
  

