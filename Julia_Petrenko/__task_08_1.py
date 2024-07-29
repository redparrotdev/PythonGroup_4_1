from converters import *


def convert_amount():
    amount = float(input("Enter amount (BYN): "))
    currency = input("Enter currency (RUB, EUR, USD): ")

    if currency.upper() == "RUB":
        return rub_converter.converter(amount)
    elif currency.upper() == "EUR":
        return eur_converter.converter(amount)
    elif currency.upper() == "USD":
        return usd_converter.converter(amount)
    else:
        print("Check your enter of currency. It must be RUB or EUR or USD")


print(convert_amount())
