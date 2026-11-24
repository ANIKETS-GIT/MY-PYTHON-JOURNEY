# 1. Salary Slip Generator
# An employee has basic_salary = 50000. HRA is 40% of basic, PF deduction is 12% of basic, and income tax is 10% of (basic + HRA). 
# Calculate gross salary, total deductions and net take-home salary.

salary = 50000
hra = 40/100*salary
pf = 12/100*salary
income_tax = (salary + hra)/100*10
gross_salary = salary+hra
total_deduction = pf+income_tax
print("gross_salary : ",gross_salary)
net_take_home_salary = gross_salary-(pf+income_tax)
print("net_take_home_salary : ",net_take_home_salary)
print("total deductions : ",total_deduction)







