monthly_income = input ("Enter your monthly income:")
monthly_expenses = input ("Enter your total monthly expenses:")

monthly_savings = int (monthly_income) - int (monthly_expenses)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print (monthly_savings)
print (projected_savings)