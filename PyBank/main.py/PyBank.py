#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("../Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("../analysis", "budget_analysis.txt")  # Output file path


# In[39]:


#Reading file to load
import csv

#define variable
total = 0
total_months = 0
net_profit_losses = 0
average_profit_losses = 0
previous_profit_loss = 0
row_number = 0
total_change_in_profit_losses = 0
greatest_profit_increase = 0
greatest_profit_increase_month = ''
greatest_profit_decrease = 0
greatest_profit_decrease_month = ''


#opening file 
with open (file_to_load, "r") as file:
    csv_reader = csv.reader (file)
    next (csv_reader)
    for row in csv_reader:
        net_profit_losses = net_profit_losses+ int(row [1])

        #net change of profit/loss and average change 
        if total_months != 0:
            monthly_change = (int(row [1]) -  previous_profit_loss)
            total_change_in_profit_losses = total_change_in_profit_losses + monthly_change
            if monthly_change > greatest_profit_increase:
                greatest_profit_increase = monthly_change
                greatest_profit_increase_month = row [0]
                
            if monthly_change < greatest_profit_decrease:
                greatest_profit_decrease = monthly_change
                greatest_profit_decrease_month = row [0]
                
           
        previous_profit_loss = int(row [1])
        total_months = total_months + 1
        
    #Total months and net  profit/loss                                      
    print (total_months)
    print (net_profit_losses)
    
    #Profit loss over entire time
    average_profit_losses =  total_change_in_profit_losses/ (total_months - 1)
    print(average_profit_losses)
    
    # greatest profit increase and decrease
    print(greatest_profit_increase)
    print(greatest_profit_decrease)
    
# exproting in txt file
with open (file_to_output, "w") as file:
    file.write('Financial Analysis\n')
    file.write ('----------------------------\n')
    file.write('Total months:' + str(total_months) + '\n')
    file.write('Total: $' + str(net_profit_losses) + '\n')  
    file.write('Average Change: $' + str(average_profit_losses) + '\n')
    file.write('Greatest Increase in Profits:' + str(greatest_profit_increase_month) + ' ($'+ str(greatest_profit_increase)+')' + '\n')
    file.write('Greatest Decrease in Profits:' + str(greatest_profit_decrease_month) + ' ($'+ str(greatest_profit_decrease)+')' + '\n')
    


 


# In[ ]:




