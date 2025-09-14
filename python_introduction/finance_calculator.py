#declaring the relevant variables

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#relevant arithmetic operations

monthly_savings = monthly_income - monthly_expenses
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#printing out the results on the console

print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_annual_savings)
