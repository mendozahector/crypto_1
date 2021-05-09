class Crypto:
    def __init__(self, name, acronym, amount):
        self.name = name
        self.acronym = acronym
        self.amount = amount

def digital_wallet():
    cryptos = list()

    dollars = Crypto('Dollars', 'USD', 4577)
    bitcoin = Crypto('Bitcoin', 'BTC', 3.578)
    ethereum = Crypto('Ethereum', 'ETH', 1.23)
    dogecoin = Crypto('Dogecoin', 'DOGE', 12.245)

    cryptos.append(dollars)
    cryptos.append(bitcoin)
    cryptos.append(ethereum)
    cryptos.append(dogecoin)

    def print_money():
        print("Your current digital wallet:\n")

        for crypto in cryptos:
            print(f"{crypto.name} - {crypto.acronym}: {crypto.amount}")

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
                print(f"We have added ${deposit} to your wallet. Thank you.\n")
                cryptos[0].amount += deposit

                print_money()
                print(menu)
            elif choice == 2:
                withdraw = float(input(f"Enter the amount to withdraw (up to ${cryptos[0].amount}): "))

                if withdraw > 0 and withdraw <= cryptos[0].amount:
                    cryptos[0].amount -= withdraw
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
    print("Displaying crypto charts...\n")

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
        elif choice == 3:
            crypto_trading()
        else:
            raise ValueError
    except ValueError:
        print(choice)
        print("Invalid option. Please try again.")