class Customer:

    def __init__(self, customer_id:str, personal_nbr:str, name:str):
        self._customer_id = customer_id
        self._personal_nbr = personal_nbr
        self._name = name

    def get_customer_id(self):
        return self._customer_id
    
    def get_personal_nbr(self):
        return self._personal_nbr
    
    def get_name(self):
        return self._name

    def __str__(self):
        return f"{self._name}, Kundnummer: {self._customer_id}, Personnr: {self._personal_nbr}"

class Account:

    def __init__(self, customer_id, account_nbr):
        self._customer_id = customer_id
        self._account_nbr = account_nbr
        self._balance = 0

    def deposit(self, amount:float):
        if amount > 0:
            self._balance += amount
            return True
        else: 
            return False

    def withdraw(self, amount:float):
        if self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False
        
    def get_balance(self):
        return self._balance
    
    def get_customer_id(self):
        return self._customer_id

    def __str__(self):
        return f"Kontonummer: {self._account_nbr}, Saldo: {self._balance} ({self._customer_id})"

class Bank():
    latest_customer_id = 9
    latest_account_nbr = 999

    def __init__(self):
        self._customers = {}
        self._accounts = {}

    def add_customer(self, name, personal_nbr):
        for customer_id, customer in self._customers.items():
            if personal_nbr == customer.get_personal_nbr():
                return None
        Bank.latest_customer_id += 1
        self._customer_id = "C" + str(Bank.latest_customer_id)
        self._customers[self._customer_id] = Customer(self._customer_id, personal_nbr, name)
        return self._customer_id
        
    def get_customer(self, customer_id):
        return self._customers.get(customer_id)
    
    def find_customer_by_part_of_name(self, name_part:str):
        return [customer for customer in self._customers.values() if name_part.lower() in customer.get_name().lower()]
    
    def create_account(self, customer_id):
        if customer_id in self._customers.keys():
            Bank.latest_account_nbr += 1
            self._accounts[Bank.latest_account_nbr] = Account(customer_id, Bank.latest_account_nbr)
            return Bank.latest_account_nbr
        else:
            return -1
        
    def get_account(self, account_nbr):
        return self._accounts.get(account_nbr)
    
    def remove_account(self, account_nbr):
        if account_nbr in self._accounts.keys():
            if self._accounts[account_nbr].get_balance() > 0:
                return False
            else:
                del self._accounts[account_nbr]
                return True
    
    def transfer(self, from_acc_nbr:int, to_acc_nbr:int, amount:float):
        if from_acc_nbr in self._accounts.keys() and to_acc_nbr in self._accounts.keys() and amount > 0 and self._accounts[from_acc_nbr].get_balance() >= amount:
            self._accounts[from_acc_nbr].withdraw(amount)
            self._accounts[to_acc_nbr].deposit(amount)
            return True
        else:
            return False
        
    def all_accounts(self):
        return [account for account in self._accounts.values()]
    
    def account_by_customer(self, customer_id):
        return [account for accountnr, account in self._accounts.items() if customer_id == account.get_customer_id()] or None

    def all_customers_sorted_by_name(self):
        return sorted(self._customers.values(), key=lambda customer: customer.get_name())
