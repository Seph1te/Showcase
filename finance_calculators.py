#=====================finance_calculator=====================#
# This program gives the user the choice between a home loan #
# repayment and an investment calculator.                    #
#============================================================#

import math

print("investment".ljust(10),"- to calculate the amount of interest you'll earn on your investment")
print("bond".ljust(10),"- to calculate the amount you'll have to pay on a home loan")
print("")

chosen_program = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n")

# if the user chooses 'bond'
if (chosen_program.lower() == "bond"):

    house_value = float(input("Please enter the value of the property. e.g. 100000.\n"))
    # formatting to always show two decimal places after the comma
    formatted_house_value = "{:.2f}".format(house_value)                                     
    int_rate = float(input("Please enter the yearly interest rate. e.g. 7.\n"))
    monthly_int_rate = ((int_rate/100)/12)
    repay_months = int(input("Please enter the numbers or months over which you plan to repay the bond. e.g. 120. \n"))

    # calculation of the monthly repayments
    repayment = (monthly_int_rate * house_value)/(1 - (1 + monthly_int_rate) ** (-repay_months))
    formatted_repayment = "{:.2f}".format(repayment)

    # output for bond repayments
    print("")
    print("=============================================================")
    print(f"Value of the property: £{formatted_house_value}")
    print(f"Yearly interest rate: {int_rate}%")
    print(f"Your monthly payments will be £{formatted_repayment} for {repay_months} months.")
    print("=============================================================")
    print("")
    
# if the user chooses 'investment'
elif (chosen_program.lower() == "investment") or (chosen_program.lower() == "inv"):

    inv_amount = float(input("How much money would you like to invest? e.g. 100000. \n"))
    formatted_inv_amount = "{:.2f}".format(inv_amount)
    inv_int_rate = float(input("At which interest rate are you looking to invest? Enter '8' for '8%'.\n"))
    inv_years = float(input("For how many years would you like to invest? e.g. 7. \n"))
    interest = input("Please choose between the 'simple' and 'compound' interest method. Enter 'simple' or 'compound' to proceed.\n")

    # if the user chooses 'simple' interest for their investment
    if (interest.lower() == "simple"):
        
        # calculations for the simple method
        inv_total_amount = inv_amount * (1 + ((inv_int_rate/100) * inv_years))
        formatted_inv_total_amount = "{:.2f}".format(inv_total_amount)                                  
        gained_amount = inv_total_amount - inv_amount
        formatted_gained_amount = "{:.2f}".format(gained_amount)

        # output for the simple method
        print("")
        print("You chose the 'simple' interest method for your investment.")
        print("=============================================================") 
        print(f"Investment: £{formatted_inv_amount}")
        print(f"Yearly interest rate: {inv_int_rate}%") 
        print(f"Duration of investment in years: {inv_years}")
        print(f"Chosen interest method: {interest} method")
        print("")                                       
        print(f"Your payout after {inv_years} years will be £{formatted_inv_total_amount}.")
        print(f"This is a gain of £{formatted_gained_amount}.")
        print("=============================================================") 
        print("")

    # if the user chooses 'compound' interest for their investment
    elif (interest.lower() == "compound"):
       
        # calculations for the compound method
        inv_total_amount = inv_amount * math.pow((1 + (inv_int_rate/100)),inv_years)
        formatted_inv_total_amount = "{:.2f}".format(inv_total_amount)                                 
        gained_amount = inv_total_amount - inv_amount
        formatted_gained_amount = "{:.2f}".format(gained_amount)

        # output for the compound method
        print("")
        print("You chose the 'compound' interest method for your investment.")
        print("=============================================================")
        print(f"Investment: £{formatted_inv_amount}")
        print(f"Yearly interest rate: {inv_int_rate}%") 
        print(f"Duration of investment in years: {inv_years}")
        print(f"Chosen interest method: {interest} method")
        print("")                                           
        print(f"Your payout after {inv_years} years will be £{formatted_inv_total_amount}.")
        print(f"This is a gain of £{formatted_gained_amount}.")
        print("=============================================================") 
        print("")

    else:
        print("The chosen interest method could not be recognised. Please restart the program and try again.")
        print("") 

else:
    print("The chosen program could not be recognised. Please restart the program and try again.")
    print("")