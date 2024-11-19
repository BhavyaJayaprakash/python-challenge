
#import os and csv module
import os
import csv

#make variable for total months in dataset
#make variable for total profits/losses in dataset
#make variable for average change in dataset
total_months = []
total_amount = []
average_change = []

#Read in csv module
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

#Open CSV file and process it 
with open(csvpath,encoding="utf-8") as csvfile:

    #File Delimited by commas
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    #Skip the header row
    csv_header = next(csvreader)

   #Loopimg rows in the data set to process it

   #Append rows for month count & sum total 
    for row in csvreader:

        total_months.append(row[0])
        total_amount.append(int(row[1]))

        #Looping through each profit change to calculate average change
    for i in range(len(total_amount)-1):
        average_change.append(total_amount[i+1]-total_amount[i])

#Declare variables for greatest increase & greatest decrease in dataset
greatest_increase = max(average_change)
greatest_decrease = min(average_change)   

#Append greatest increase & greatest decrease to corresponding months and add 1 for max & min calculation
greatest_increase_month = average_change.index(max(average_change)) + 1
greatest_decrease_month = average_change.index(min(average_change)) + 1

#Printing data analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {len(total_months)}" )
print(f"Total: ${sum(total_amount)}")

#Calculate average change by SUM of changes/AMount of changes. Round to two decimal points
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")

#Formatting the data for greatest increase/decrease values and adding dollar sign, and attach  months
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")
        
#Exporting the data analysis to a text file
analysis = os.path.join("Analysis", "Financial_Analysis.txt")
#analysis = os.path.join('c:/Users/shank/OneDrive/Desktop/NU-VIRT-DATA-PT-10-2024-U-LOLC/02-Homework/03-Python/python-challenge/PyBank/analysis/Financial_Analysis.txt')
with open(analysis,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months : {len(total_months)}" )
    file.write("\n")
    file.write(f"Total: ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")
        
#End