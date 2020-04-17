import os
import csv

read_path = os.path.join("Resources", "budget_data.csv")

months = 0
profit_loss = 0
average_change = 0.00
max_inc = 0
max_dec = 0
max_inc_month = ""
max_dec_month = ""
this_month = 0
last_month = None
changes = []
rate_change = 0
month_name = ""

with open(read_path, newline = "", encoding = "utf8") as temp_file:
    budget_data = csv.reader(temp_file, delimiter = ",")

    #read the header row first (skip if there is no header)
    data_header = next(temp_file)

    #run through each row in csv file
    for row in budget_data:
        this_month = int(row[1])    #identify this month's revenue
        month_name = row[0]         #identify current month
        months += 1                 #count the months
        profit_loss += this_month   #add monthly revenue to total
        
    #average_change = profit_loss / months
        if last_month is not None: #do not check on first month; no change
            rate_change = (this_month-last_month) #calculate change in rate from previous month
            changes.append(rate_change) #add change to list of month changes
            if rate_change > max_inc:   #if current change rate is highest,
                max_inc = rate_change   #overwrite max rate with new value
                max_inc_month = month_name
            elif rate_change < max_dec: #if current change rate is lowest,
                max_dec = rate_change   #overwrite max decrease with new value
                max_dec_month = month_name
        last_month = this_month       #current month becomes last month for next loop
    average_change = sum(changes)/len(changes)  #calculate average monthly revenue change

#print results
print(f"Total Months: {months}\nTotal: ${profit_loss}\nAverage Change: ${round(average_change, 2)}\nGreatest Increase in Profits: {max_inc_month} (${max_inc})\nGreatest Decrease in Profits: {max_dec_month} (${max_dec})")

# Specify the file to write to
write_path = os.path.join("output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(write_path, "w") as output_file:
    output_file.write(f"Total Months: {months}\nTotal: ${profit_loss}\nAverage Change: ${round(average_change, 2)}\nGreatest Increase in Profits: {max_inc_month} (${max_inc})\nGreatest Decrease in Profits: {max_dec_month} (${max_dec})")