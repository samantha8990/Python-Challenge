import os
import csv

#get file path
pybank_path= os.path.join('PyBank','Resources','pybank.csv')
#pybank_path= os.path.join('Resources','pybank.csv')

#open file
with open(pybank_path) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    header=next(csv_reader)
    # csv_reader ==== (Date,Profit/Losses)

#set variables
    months=[]
    profit=[]
    changes=[]
    max_profit=0
    min_profit=0
  
    for row in csv_reader:
        months.append(row[0])
        profit.append(int(row[1])) #this add all of column profit/losses

    for i in range(1, len(profit)): 
        # len(profit) ====== 86
        # range(86) ======== [0, 1, 2, .... 85]
        changes.append(profit[i]-profit[i-1])
        #     profit[0]-profit[-1] trying to avoid this one
#     profit[1]-profit[0]
#     profit[2]-profit[1]
#     profit[3]-profit[2]
#     profit[85]-profit[84]

    for change in changes: # changes ====== [15000, 62000, ...., 43214321]
        if change > max_profit: # if element of list is greater than placeholder
            max_profit=change # then found new max
        else: 
            pass
    for change in changes: # changes ====== [15000, 62000, ...., 43214321]
        if change < min_profit: # if element of list is greater than placeholder
            min_profit=change # then found new max
        else: 
            pass
        

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:", len(months))
    print("Total:", sum(profit))
    print("Average Change:", sum(str(changes)/len(changes))
    print("Greatest Increase in Profits:", max_profit)
    print("Greatest Decrease in Profits:", min_profit)
<<<<<<< HEAD



=======
>>>>>>> 25f166a81c1e23c665f106bdc90148d978bd0238
