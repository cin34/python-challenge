# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
max_profit = ["", 0]
max_loss = ["", 0]
net_change_list = []
last_profit = 0

# Open and read the csv
with open(file_to_load, encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        row[1] = int(row[1])

        # Tracking the totals
        total_months += 1
        total_net += row[1]
        current_profit = row[1]

        # Track the net change
        if total_months > 1:
            change = (row[1] - last_profit)
            net_change_list.append(change)

            # Calculate the greatest increase in profits (month and amount)
            if change > max_profit[1]:
                max_profit[1] = change
                max_profit[0] = row[0]

            # Calculate the greatest decrease in losses (month and amount)
            if change < max_loss[1]:
                max_loss[1] = change
                max_loss[0] = row[0]
        last_profit = row[1]    

# Calculate the average net change across the months
average_net = sum(net_change_list)/len(net_change_list)

# Print the output
output = (f"Financial Analysis\n"
          f"------------------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${total_net}\n"
          f"Average Change: ${average_net:.2f}\n"
          f"Greatest Increase in Profits: {max_profit[0]} (${max_profit[1]})\n"
          f"Greatest Decrease in Profits: {max_loss[0]} (${max_loss[1]})\n")
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
