class ATM:
 def __init__(self, balance):
    self.balance = balance

 def display_balance(self):
    print(f"Your current balance is: ${self.balance}")

 def cash_in(self, amount):
    self.balance += amount
    print(f"You have deposited ${amount}.")
    self.display_balance()
    self.print_receipt(amount, "Deposit")

 def cash_out(self, amount):
    if self.balance >= amount:
        self.balance -= amount
        print(f"You have withdrawn ${amount}.")
        self.display_balance()
        self.print_receipt(amount, "Withdrawal")
    else:
        print("Insufficient funds.")

 def print_receipt(self, amount, transaction_type):
    print(f"Receipt - {transaction_type}: ${amount}")

# Example usage
if __name__ == "__main__":
    initial_balance = 1000
    atm = ATM(initial_balance)

    atm.display_balance()
    atm.cash_in(500)
    atm.cash_out(200)