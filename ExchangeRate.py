import csv

class ExchangeRate:
    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()

    def convert(self):                                                          # reads exchange rate in csv file
        with open('BankOfCanadaExchangeRates.csv', mode='r') as file:
            csvreader = csv.DictReader(file)
            rows = list(csvreader)
            last_row = rows[-1]                                                 # use most recent exchange rate
            usd_cad_rate = float(last_row['USD/CAD'])                           # reads the last column 

            # Perform conversion
            if self.from_currency == "USD" and self.to_currency == "CAD":
                converted = self.amount * usd_cad_rate
            elif self.from_currency == "CAD" and self.to_currency == "USD":
                converted = self.amount / usd_cad_rate
            else:
                print("Conversion not supported. Only USD and CAD supported.")

            return round(converted, 2)                                          # returns round


# Main Execution
if __name__ == "__main__":
    print("Currency Conversion")
    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD/CAD): ")
    to_currency = input("Convert to (USD/CAD): ")

    exchange = ExchangeRate(amount, from_currency, to_currency)
    result = exchange.convert()

# Final result
    print("Conversion result: " + str(result))
