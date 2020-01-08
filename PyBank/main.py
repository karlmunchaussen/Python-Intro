import csv
from pathlib import Path

csvpath = Path("/Users/leonzubkov/Desktop/pyth-homework/PyBank/Data/budget_data.csv")

count_cycles = 0
net_total = 0
last_cycle_p_l = 0
profit_loss = 0
change = 0
max_change = 0                                
max_change_date = []
min_change = 0                                
min_change_date = []
total_change = 0

with open(csvpath, 'r') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    next(csvreader)                            

    for row in csvreader:
        profit_loss = int(row[1])              
        count_cycles += 1                     
        net_total += int(row[1])       

        if last_cycle_p_l == 0:        
            last_cycle_p_l = profit_loss

        change = profit_loss - last_cycle_p_l  
        total_change += change                 
        if change > max_change:                
            max_change = change
            max_change_cycle = row[0]
        if change < min_change:                
            min_change = change
            min_change_cycle = row[0]
        last_cycle_p_l = profit_loss   
budget_data.close()                                   

analysis = (f"\
Financial analysis\n\n\
--------------------\n\n\
Total Months:  {count_cycles}\n\
Total:   ${net_total}\n\
Average change:  ${round(total_change / (count_cycles-1), 2)}\n\
The greatest increase in profits over the entire period: {max_change_date} (${max_change})\n\
The greatest decrease in profits over the entire period: {min_change_date} (${min_change})")

print(analysis)

output_csv = Path("/Users/leonzubkov/Desktop/pyth-homework/PyBank/report.csv")

with open(output_csv, 'w') as report:
    report.write(analysis)

report.close()
