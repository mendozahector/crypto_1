from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class Currency:
    def __init__(self, name, symbol, amount):
        self.name = name
        self.symbol = symbol
        self.amount = amount

def digital_wallet():
    wallet = list()

    dollars = Currency('Dollars', 'USD', 4577)
    bitcoin = Currency('Bitcoin', 'BTC', 3.578)
    ethereum = Currency('Ethereum', 'ETH', 1.23)
    dogecoin = Currency('Dogecoin', 'DOGE', 12.245)

    wallet.append(dollars)
    wallet.append(bitcoin)
    wallet.append(ethereum)
    wallet.append(dogecoin)

    def print_money():
        print("Your current digital wallet:\n")

        for currency in wallet:
            print(f"{currency.name} - {currency.symbol}: {currency.amount}")

    menu = """\nPlease select an option:
    1. Deposit
    2. Withdraw
    0. Main Menu"""

    print_money()
    print(menu)

    choice = None
    while choice != 0:
        try:
            choice = int(input("> "))
            if choice == 0:
                break
            elif choice == 1:
                deposit = float(input("Please enter your amount in dollars (USD): "))

                if deposit > 0:
                    print(f"We have added ${deposit} to your wallet. Thank you.\n")
                    wallet[0].amount += deposit
                else:
                    print("Please enter an amount greater than zero.")

                print_money()
                print(menu)
            elif choice == 2:
                withdraw = float(input(f"Enter the amount to withdraw (up to ${wallet[0].amount}): "))

                if withdraw > 0 and withdraw <= wallet[0].amount:
                    wallet[0].amount -= withdraw
                    print("Success. Please allow 2-3 business days for transaction to process.")
                else:
                    print("Invalid withdraw amount. Please try again.\n")
                
                print_money()
                print(menu)
            else:
                raise ValueError
        except ValueError:
            print(choice)
            print("Invalid option. Please try again.")

def crypto_charts():
    print("Retrieving crypto data...\n")

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'10',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7aff45c2-193a-46b5-8ac8-9d4a15b27879',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        for crypto in data['data']:
            print(f"* {crypto['name']} - {crypto['symbol']}: $ {crypto['quote']['USD']['price']:.4f}")

        out_file = open("cryptodata.json", "w")
        json.dump(data, out_file, indent = 6)
        out_file.close()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    print()

def crypto_trading():
    print("Ready to trade?\n")

menu = """Welcome to your Crypto Exchange Market. Please select an option:
    1. My Digital Wallet
    2. Crypto Charts
    3. Crypto Trading
    0. Exit"""

print(menu)

choice = None
while choice != 0:
    try:
        choice = int(input("> "))
        if choice == 0:
            break
        elif choice == 1:
            digital_wallet()
            print(menu)
        elif choice == 2:
            crypto_charts()
            print(menu)
        elif choice == 3:
            crypto_trading()
        else:
            raise ValueError
    except ValueError:
        print(choice)
        print("Invalid option. Please try again.")