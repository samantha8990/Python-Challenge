import os
import csv


#get file path
pybank_path= os.path.join('PyBank','Resources','pybank.csv')


#open file
with open(pybank_path) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    csv_reader=next(csv_file)


    #set variables
def total(pybank_path):
    date=(bank_data[0])
    profit_losses=int(bank_data[1])

    total_rev=sum(profit_losses)
    print(total_rev)
