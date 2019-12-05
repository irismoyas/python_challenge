import os
import csv

print(os.path.abspath(__file__))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath=os.path.join("resources","budget_data.csv")   

total_months = 0
net_total_amount = 0
prev_amount = 0
monthly_change = 0
total_monthly_change = 0
average_monthly_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_increase_month = ""

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    cvs_header=next(csvreader)
    
    for row in csvreader:
        total_months+=1
        net_total_amount+=int(row[1])
        
        if total_months>1:
            monthly_change=int(row[1])-prev_amount
        total_monthly_change+=monthly_change
        prev_amount=int(row[1])
        if monthly_change>greatest_increase:
            greatest_increase=monthly_change
            greatest_increase_month=row[0]
        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_month = row[0]
average_monthly_change = round(total_monthly_change / (total_months - 1),2)

print("Financial Analysis")
print("----------------------------")        
print("Total Months: " +str(total_months))
print("Total: $" + str(net_total_amount))
print("Average Change: $" + (str(average_monthly_change)))
print("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")")

f = open("financial analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n") 
f.write("Total: $" + str(net_total_amount) + "\n")
f.write("Average Change: $" + str(average_monthly_change) + "\n")
f.write("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")\n")
f.close()