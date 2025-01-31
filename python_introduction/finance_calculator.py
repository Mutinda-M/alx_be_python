monthly_income = input ("Enter your monthly income:")
monthly_expenses = input ("Enter your total monthly expenses:")

monthly_savings = int (monthly_income) - int (monthly_expenses)

annual_rate = 0.05 #5% annual intrest rate

annual_savings_projection = monthly_savings * 12 + (monthly_savings * 12 * annual_rate)

print (monthly_savings)
print (annual_savings_projection)