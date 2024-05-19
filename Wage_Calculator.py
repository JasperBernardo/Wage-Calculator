def wage_calculator():
    # Get user input for hourly wage and hours worked per week
    hourly_wage = float(input("Enter your hourly wage: $"))
    hours_per_week = float(input("Enter the number of hours you work per week: "))

    # Calculate weekly, monthly, and yearly wages
    weekly_wage = hourly_wage * hours_per_week
    monthly_wage = weekly_wage * 4  # Assuming 4 weeks in a month
    yearly_wage = weekly_wage * 52  # Assuming 52 weeks in a year

    # Display the results
    print(f"\nWage Calculation:")
    print(f"Weekly Wage: ${weekly_wage:.2f}")
    print(f"Monthly Wage: ${monthly_wage:.2f}")
    print(f"Yearly Wage: ${yearly_wage:.2f}")

if __name__ == "__main__":
    wage_calculator()
