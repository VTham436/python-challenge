import os
import csv


pybank_csv = os.path.join("../PyBank/Resources/budget_data.csv")

#Track Variables
total_months = []
total_profit = []
average_change = []
greatest_increase = []
greatest_decrease = []

#Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #Read header row first
    csv_header = next(csv_reader)
        
    for row in csv_reader:
    #Add months starting from 1st column
        total_months.append(row[0])
        #Adding all profit values, positive and negative
        total_profit.append(int(row[1]))

    #Find the average change
    for i in range(len(total_profit)-1):
        average_change.append(total_profit[i+1] - total_profit[i])

    #Greatest increase and decrease
    greatest_increase = max(average_change)
    greatest_decrease = min(average_change)
    #Dates for greatest increase and decrease
    max_month = average_change.index(max(average_change)) + 1
    min_month = average_change.index(min(average_change)) + 1    
        
#Print statements        
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Profit: ${sum(total_profit)}")
print(f"Average Change: $ {round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_month]} (${(str(greatest_increase))}")
print(f"Greatest Decrease in Profits: {total_months[min_month]} (${(str(greatest_decrease))}")

#Export text file
output_file = ("../PyBank/Analysis.txt")

with open(output_file,"w") as file:
    
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total Profit: ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(average_change)/len(average_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_month]} (${(str(greatest_increase))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_month]} (${(str(greatest_decrease))})")