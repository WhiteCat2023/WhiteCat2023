import datetime,os,time

class ATM:
    def __init__(account):
        account.balance = 100 # Default balance is $100

    def display_balance(account):
        print(f"\033[32mYour balance is: ${account.balance}\033[0m")
        time.sleep(1)
        os.system("cls")
    def withdraw_cash(account, amount):
        if amount <= account.balance:
            account.balance -= amount
            print("\033[32m=========== BANK OF 1 ===========\033[32m")
            now = datetime.datetime.now()
            print("\033[32mDate:", now.strftime("%y-%m-%d\033[0m"))
            now = datetime.datetime.now()
            print("\033[32mTime:", now.strftime("%H:%M:%S\033[0m"))
            print("\033[32m========================================\033[0m")
            print()
            print("\033[32mard: ***********2343")
            print("Seg. Num: 1234")
            print("Withdraw From: 7 ELEVEN ")
            print(f"Amount: ${amount}")
            print()
            print(f"Account Balance: ${account.balance}")
            print(f"AVAILABLE BALANCE: ${account.balance}")
            print()
            print("PLEASE RETAIN OR DISPOSE OF IT THOUGHTFULLY\033[0m")
            time.sleep(2)
            os.system("cls")
        else:
            print("\033[31mInsufficient balance.\033[0m")
            time.sleep(1)
            os.system("cls")

    def deposit_cash(account, amount):
        account.balance += amount
        print(f"\033[32mDeposited ${amount} successfully.\033[0m")
        time.sleep(1)
        os.system("cls")
        print("\033[32m=========== BANK OF ANY NAME ===========")
        now = datetime.datetime.now()
        print("Date:", now.strftime("%y-%m-%d"))
        now = datetime.datetime.now()
        print("Time:", now.strftime("%H:%M:%S"))
        print("========================================")
        print()
        print("Card: ***********2343")
        print("Seg. Num: 1234")
        print("Deposit From: BDO")
        print(f"Amount: ${amount}")
        print()
        print(f"Account Balance: ${account.balance}")
        print(f"AVAILABLE BALANCE: ${account.balance}")
        print()
        print("PLEASE RETAIN OR DISPOSE OF IT THOUGHTFULLY\033[0m")
        time.sleep(2)
        os.system("cls")
    def main_menu(account):
        while True:
            print("\n\033[32mMain Menu:")
            print("1. Check Balance")
            print("2. Withdraw Cash")
            print("3. Deposit Cash")
            print("4. Quit")

            choice = float(input("Select menu Transaction (1-4): \033[0m"))
            os.system("cls")
            if choice == 1:
                account.display_balance()
            elif choice == 2:
                account.withdraw_menu()
            elif choice == 3:
                deposit_amount = float(input("\033[32mEnter Deposit Amount: $"))
                account.deposit_cash(deposit_amount)
                os.system("cls")
            elif choice == 4:
                print("\033[32mThank you for using Robinsons Bank.")
                break
            else:
                print("\033[31mInvalid choice. Please select a valid option.\033[0m")
                time.sleep(1)
                os.system("cls")
    def withdraw_menu(account):
        print("\n\033[32mWithdraw Menu:")
        print("1. $10")
        print("2. $20")
        print("3. $50")
        print("4. $100")
        print("5. Enter amount")
        choice = float(input("Choose withdraw amount (1-5): "))
        os.system("cls")
        if choice == 1:
            account.withdraw_cash(10)
        elif choice == 2:
            account.withdraw_cash(20)
        elif choice == 3:
            account.withdraw_cash(50)
        elif choice == 4:
            account.withdraw_cash(100)
        elif choice == 5:
            wd = float(input("\033[32mEnter withdraw amount: "))
            os.system("cls")
            if wd > account.balance:
                print("\033[31mInsufficient balance.\033[0m")
                time.sleep(1)
                os.system("cls")
            else:
                account.withdraw_cash(wd)
        else:
            print("\033[31mInvalid choice. Please select a valid option.\033[0m")
            time.sleep(1)
            os.system("cls")

    def date_now():
        now = datetime.datetime.now()
        print("Date:", now.strftime("%y-%m-%d"))
    def time_now():
        now = datetime.datetime.now()
        print("Time:", now.strftime("%H:%M:%S"))
    


if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()