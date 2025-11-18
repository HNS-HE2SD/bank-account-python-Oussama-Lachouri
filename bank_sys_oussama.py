import os
# Class Client
class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.accounts = []
    # Getters and setters for all attributes
    def get_CIN(self): return self.__CIN
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_tel(self): return self.__tel

    def set_tel(self, tel): self.__tel = tel
    def add_account(self, account):
        self.accounts.append(account)
    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")
    def displayAccounts(self):
        print("Accounts:")
        for account in self.accounts:
            account.display()
# Class Account
class Account:
    __nbAccounts = 0  # static variable for sequential codes

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.history=[]
    # Access methods
    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

    # Credit and debit methods
    def credit(self, amount, account=None):
      if amount <= 0:
          print("Amount must be positive.")
          return
      else:
        if account is None:
            self.__balance += amount
            self.history.append(f"Credited: {amount} DA")
        else:
            if account.get_balance() < amount:
                print("Insufficient balance in the source account.")
                return
            else:
             self.__balance += amount
             account.debit(amount)
             self.history.append(f"Received: {amount} DA from Account {account.get_code()}")
    def debit(self, amount, account=None):
      if amount <= 0:
          print("Amount must be positive.")
          return
      else:
        if self.__balance >= amount:
            self.__balance -= amount
            self.history.append(f"Debited: {amount} DA")
            if account is not None:
                account.credit(amount)
                self.history.append(f"Sent: {amount} DA to Account {account.get_code()}")
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")
    
    def displayTransaction(self):
       print("Transaction History:")
       for i in self.history:
           print(i)

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)


# -------- MENU ---------

clients = []   # List of Client objects
accounts = []  # List of Account objects


def find_client(cin):
    for c in clients:
        if c.get_CIN() == cin:
            return c
    return None

def find_account(code):
    for a in accounts:
        if a.get_code() == code:
            return a
    return None


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n===== BANK MENU =====")
    print("1 - Add Client")
    print("2 - Create Account")
    print("3 - Credit Account")
    print("4 - Debit Account")
    print("5 - Transfer Between Accounts")
    print("6 - Display Client Info")
    print("7 - Display Account Info")
    print("8 - Display Account Transactions")
    print("9 - Display Total Number of Accounts")
    print("10 - Exit")
    choice = input("Enter your choice: ")

    # Add Client
    if choice == "1":
        cin = input("CIN: ")
        first = input("First name: ")
        last = input("Last name: ")
        tel = input("Tel: ")

        c = Client(cin, first, last, tel)
        clients.append(c)
        print("Client added successfully!")
        input("press Enter to continue...")

    # Create Account
    elif choice == "2":
        cin = input("Enter CIN of client: ")
        c = find_client(cin)
        if c is None:
            print("Client not found!")
        else:
            acc = Account(c)
            c.add_account(acc)
            accounts.append(acc)
            print("Account created! Code:", acc.get_code())
        input("press Enter to continue...")
    # Credit Account
    elif choice == "3":
        code = int(input("Account code: "))
        acc = find_account(code)
        if acc:
            amount = float(input("Amount to credit: "))
            acc.credit(amount)
        else:
            print("Account not found.")
        input("press Enter to continue...")
    # Debit Account
    elif choice == "4":
        code = int(input("Account code: "))
        acc = find_account(code)
        if acc:
            amount = float(input("Amount to debit: "))
            acc.debit(amount)
        else:
            print("Account not found.")
        input("press Enter to continue...")
    # Transfer
    elif choice == "5":
        src_code = int(input("Source account: "))
        dst_code = int(input("Destination account: "))
        amount = float(input("Amount: "))

        src = find_account(src_code)
        dst = find_account(dst_code)

        if src and dst:
            src.debit(amount, dst)
        else:
            print("One of the accounts does not exist.")
        input("press Enter to continue...")
    # Display Client
    elif choice == "6":
        cin = input("CIN: ")
        c = find_client(cin)
        if c:
            c.display()
            c.displayAccounts()
        else:
            print("Client not found.")
        input("press Enter to continue...")
    # Display Account
    elif choice == "7":
        code = int(input("Account code: "))
        acc = find_account(code)
        if acc:
            acc.display()
        else:
            print("Account not found.")
        input("press Enter to continue...")
    # Display Account Transactions
    elif choice == "8":
        code = int(input("Account code: "))
        acc = find_account(code)
        if acc:
            acc.displayTransaction()
        else:
            print("Account not found.")
        input("press Enter to continue...")
    # Display Total Number of Accounts
    elif choice == "9":
        Account.displayNbAccounts()
        input("press Enter to continue...")
    #Exit        
    elif choice == "10":
        print("Goodbye!")
        input("press Enter to continue...")
        break
    else:
        print("Invalid choice. Try again.")
        input("press Enter to continue...")

