# Author: Michael Beaudet
# Title: Week 6 program 3
# Date: 2/24/25

def calculate_sales_tax(total_sales):
    state_tax_rate = 0.05
    county_tax_rate = 0.025
# Calculate the tax
    state_tax = state_tax_rate * total_sales
    county_tax = county_tax_rate * total_sales
    total_tax = county_tax + state_tax

    return state_tax, county_tax, total_tax

def main():
# Get user's input
    total_sales = float(input("Enter the total sales for this month: $"))
# Call the past function
    state_tax, county_tax, total_tax = calculate_sales_tax(total_sales)
# Print the results
    print(f"The state sales tax is: ${state_tax:.2f}")
    print(f"The county sales tax is: ${county_tax:.2f}")
    print(f"The Total sales tax is: ${total_tax:.2f}")

if __name__ == "__main__":
    main()