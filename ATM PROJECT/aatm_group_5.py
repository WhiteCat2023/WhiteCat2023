import os, time

class ATM:
    def __init__(self):
        self.balance = 100 # Default balance is $100

    def display_balance(self):
        print(f"\033[36mYour balance is: ${self.balance}\033[0m")
        time.sleep(1)
        os.system("cls")

    def withdraw_cash(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"\033[32mWithdrawn ${amount}.\033[0m")
            time.sleep(1)
            os.system("cls")
        else:
            print("\033[31mInsufficient balance.\033[0m")
            time.sleep(1)
            os.system("cls")

    def deposit_cash(self, amount):
        self.balance += amount
        print(f"\033[32mDeposited ${amount} successfully.\033[0m")
        time.sleep(1)
        os.system("cls")

    def main_menu(self):
        while True:
            print("\033[33mMain Menu:\033[0m")
            print("\033[33m1. Check Balance\033[0m")
            print("\033[33m2. Withdraw Cash\033[0m")
            print("\033[33m3. Deposit Cash\033[0m")
            print("\033[33m4. Quit\033[0m")

            choice = int(input("\033[33mSelect menu Transaction (1-4): \033[0m"))
            os.system("cls")

            if choice == 1:
                self.display_balance()
            elif choice == 2:
                self.withdraw_menu()
            elif choice == 3:
                deposit_amount = float(input("\033[33mEnter Deposit Amount: $\033[0m"))
                os.system("cls")
                self.deposit_cash(deposit_amount)
            elif choice == 4:
                print("\033[35mThank you for using the ATM. Goodbye!\033[0m")
                exit()
            else:
                print("\033[31mInvalid choice. Please select a valid option.\033[0m")
                time.sleep(1)
                os.system("cls")

    def withdraw_menu(self):
        print("""\033[33m\n
Withdraw Menu: 
1. $10 
2. $20 
3. $50 
4. $100\033[0m""")
        

        choice = int(input("\033[33mChoose withdraw amount (1-4): \033[0m"))
        os.system("cls")

        if choice == 1:
            self.withdraw_cash(10)
        elif choice == 2:
            self.withdraw_cash(20)
        elif choice == 3:
            self.withdraw_cash(50)
        elif choice == 4:
            self.withdraw_cash(100)
        else:
            print("\033[31mInvalid choice. Please select a valid option.\033[0m")
print("""\033[36m
sdfsfdsfdsfdsffdsffdsffdffdsfdsfafdsfdsfdsfdsfdfdsfdsdfdsfdsfdsfdsfdsfdsfddsasaddsa
fddsfdsfdsfdf      ddds                  dfdf     dfdfdfdsdfadfdsffd     fdsdsdsadd   
dsadsfdsfdsf  dff   dsfdsfdsfds   dsfdsfdsfdf      dfsdfdffdsfdsfff      dfdsfdssdd
dsfdsfsdfds  dsfdf  dsfdsfsfsdf   dsfdsfsdffd       dfdfdfdfdsfdsf       dfdsfdsfsd
fdsfdsfddfd  dfsff  dsfdsfdsfds   dsfdsfdsfdf   d    dfdfffdfdsfd    f   dsfdsafdss  
dsfdsafddsf  dsfff  dsfdfsfdsff   dfsdfdsfddf   df    dfdsffdfdf    fd   dfdsfdsfds 
dsfdsfdsfds         dasfdsfdsfa   dfdsfsfdsff   dfd    dfsdffdf    dsf   dsafdfdsds   
fdsfdfdsfds  dafds  fdsdfdsfdsf   ddsfdfdsffd   dfdf    dfdsff    ddsf   dsfdsfdsfd  
fsdafdfdsds  dsfsd  dsfdfsafdff   dfdsfdsfffd   dfdff    dfds    fdfds   dfdsfdfsdd
dafsdfdsfds  dsfsd  dsfdfdsfdfd   dsfdffdsfdf   ddfdff    fd    fdsfds   fadsfsdsad
fdsfdsfdsfd  dfdsf  dfdsfdsfsds   fdsfdsfdsff   fdfsdfd        dfdsfds   dfdsfdsfds
fdsfdsfdsfdsfdsfsdfdsfdfdfdsfdsmndsbfkdjsbfdksjbhfdsjkfgdsfjkdsfksdjfhdskjfhsdhdsdd    
\033[0m""")
time.sleep(2)
os.system("cls")
print("\033[33mNow Loading...\033[0m")
time.sleep(2)
os.system("cls")

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()