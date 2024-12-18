def calculate_investment_growth(investment_value, equity_amount, expected_interest, years, is_compound, dividend_amount, dividend_frequency, coupon_percentage):
    # Calculate the total return based on investment value and equity amount
    total_return = investment_value * equity_amount
    
    if is_compound:
        # Calculate the final value using compound interest formula
        final_value = total_return * ((1 + (expected_interest / 100)) ** years)
        
        # Calculate total dividends based on frequency
        if dividend_frequency == 'm':
            total_dividends = dividend_amount * 12 * years
        elif dividend_frequency == 'q':
            total_dividends = dividend_amount * 4 * years
        elif dividend_frequency == 'sa':
            total_dividends = dividend_amount * 2 * years
        elif dividend_frequency == 'a':
            total_dividends = dividend_amount * years
        else:
            total_dividends = 0
        
        # Add dividends to the final value
        final_value += total_dividends
        
        # Return total dividends for stock
        return total_dividends, final_value
    else:
        # Calculate the expected growth based on the expected interest over the specified years
        expected_growth = total_return * (expected_interest / 100) * years
        final_value = total_return + expected_growth
        
        # Calculate total coupon payments based on frequency
        total_coupons = 0
        if coupon_percentage > 0:
            if dividend_frequency == 'm':
                total_coupons = (investment_value * (coupon_percentage / 100)) / 12 * 12 * years
            elif dividend_frequency == 'q':
                total_coupons = (investment_value * (coupon_percentage / 100)) / 4 * 4 * years
            elif dividend_frequency == 'sa':
                total_coupons = (investment_value * (coupon_percentage / 100)) / 2 * 2 * years
            elif dividend_frequency == 'a':
                total_coupons = (investment_value * (coupon_percentage / 100)) * years
        
        # Add coupon payments to the final value for bonds
        final_value += total_coupons
        
        return total_coupons, final_value


# Get user inputs
share_or_bond_name = input("Enter the name of your holding: ")
investment_type = input("Is this investment a stock/share or a bond? (Enter 'stock' or 'bond'): ").strip().lower()
is_compound = investment_type == 'stock'  # Assume compounding for stocks, simple for bonds
investment_value = float(input("Enter the investment value at purchase or average price: "))
equity_amount = float(input("Enter the equity amount \n(This is the number of shares or bonds you have purchased): "))
expected_interest = float(input("Enter the expected percentage interest growth as a number: "))
years = int(input("Enter the number of years you plan to hold the investment: "))

# If the investment is a stock, ask for dividend information
dividend_amount = 0
dividend_frequency = 0
coupon_percentage = 0
if is_compound:
    dividend_amount = float(input("Enter the dividend amount received per share: "))
    dividend_frequency = input("Enter the dividend frequency (monthly, quarterly, semi-annually, annually): ").strip().lower()
else:
    coupon_percentage = float(input("Enter the coupon payout percentage: "))
    dividend_frequency = input("Enter the coupon frequency (monthly: a, quarterly: q, semi-annually: sa, annually: a): ").strip().lower()

# Calculate the percentage growth and final value
total_dividends_or_coupons, final_value = calculate_investment_growth(investment_value, equity_amount, expected_interest, years, is_compound, dividend_amount, dividend_frequency, coupon_percentage)

# Display the results
if is_compound:
    print(f"\nTotal dividend earnings over {years} years: ${total_dividends_or_coupons:.2f}")
else:
    print(f"\nTotal coupon earnings over {years} years: ${total_dividends_or_coupons:.2f}")

print(f"Final value of the investment after {years} years will be: ${final_value:.2f}")
print(f"Percentage growth of your {investment_type} investment in {share_or_bond_name} over {years} years will grow by: {((final_value - (investment_value * equity_amount)) / (investment_value * equity_amount)) * 100:.2f}%")