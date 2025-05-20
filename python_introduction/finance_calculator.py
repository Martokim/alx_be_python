'''
Task Description:

You will create a script named finance_calculator.py.
This script will calculate the user’s monthly savings based on
inputted monthly income and expenses. 
It will then project these savings over a year, assuming a fixed interest rate, 
to demonstrate compound interest’s effect on savings.
'''
monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

#monthly monthly_savings
monthly_savings = monthly_income - monthly_expenses 


#Project annual savings with 5% intrest 
projected_savings = monthly_savings * 12 + (monthly_savings *12 * 0.05)

print('Your monthly savings are $', monthly_savings ,'.')
print('Projected savings after one year , with intrest , is : $', projected_savings,'.')