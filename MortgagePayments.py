class MortgagePayments:
    def __init__(self, int_rate, amortization, principal):                     #class initialization
        self.int_rate = int_rate / 100                                         # convert % to decimal
        self.amortization = amortization
        self.principal = principal

    def _payment_for(self, freq):                                              #function to calculate payment for a given compounding frequency
        r = (1 + self.int_rate / 2) ** (2 / freq) - 1                          # Effective periodic rate with semi-annual compounding
        n = self.amortization * freq                                           # total number of payments
        payment = self.principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)     #PVA calculation
        return payment

    def payments(self):                                                      #Calculates all payment frequencies and returns them as a tuple
        # Compute for each standard frequency
        monthly = self._payment_for(12)
        semi_monthly = self._payment_for(24)
        bi_weekly = self._payment_for(26)
        weekly = self._payment_for(52)

        # Rapid payments (based on monthly equivalence)
        accelearted_bi_weekly = monthly * 1 / 2
        accelerated_weekly = monthly * 1 / 4

        # Round each value and return as tuple literal
        monthly = round(monthly, 2)
        semi_monthly = round(semi_monthly, 2)
        bi_weekly = round(bi_weekly, 2)
        weekly = round(weekly, 2)
        accelearted_bi_weekly = round(accelearted_bi_weekly, 2)
        accelerated_weekly = round(accelerated_weekly, 2)

        return (monthly, semi_monthly, bi_weekly, weekly, accelearted_bi_weekly, accelerated_weekly)


# === MAIN EXECUTION ===
if __name__ == "__main__":

    principal = float(input("Enter the principal amount ($): "))                 # collecting user inputs
    int_rate = float(input("Enter the annual interest rate (%): "))
    amortization = int(input("Enter the amortization period (years): "))

    mortgage = MortgagePayments(int_rate, amortization, principal)               # create MortgagePayments object

    payments = mortgage.payments()                                               # calculates payments

    # display results
    print("--- Payments")
    print("Monthly: $"+ str(payments[0]))
    print("Semi-monthly: $" + str(payments[1]))
    print("Bi-weekly: $" + str(payments[2]))
    print("Weekly: $" + str(payments[3]))
    print("Accelerated Bi-weekly: $" + str(payments[4]))
    print("Accelerated Weekly: $" + str(payments[5]))
    print("-"*25)



        
         





        
        
    




