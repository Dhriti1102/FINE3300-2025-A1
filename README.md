# FINE3300-2025-A1
# This repository contains the calculations for part 1 and 2 of the FINE 3300 assignment- which include interest rate and exchange rate calculations

# Part 1 : Mortgage rate calculations
# This part uses user inputs to calculate mortgage payments for different periods (monthly, semi monthly, bi-weekly, weekly, accelerated bi-weekly and accelerated weekly) 
# This contains 2 functions : payment_for and payment
# payment_for function is used to calculate the PVA payment per period by calculating the effective rate and peiod
# payment function uses the payment value from the previous function and uses the frequency in a year (eg. monthly = 12) to calculate final payment amount
# the values are stored and returned as a tuple for each period


# Part 2 : Currency Conversion Calculations
# This part uses amount and currency(USD/CAD) entered by user to convert in either currency using the latest conversion rate
# Function convert() is used to read the .csv file provided and perform the conversion calculations between currencies
# Reading .csv file : by using import function and [-1] indexing to fetch the latest exchange rate in the 'USD/CAD' column
# Conversion Calculation : by using if else, we specify the necessary conditions for rate calculation

# Assumption: user input is valid


