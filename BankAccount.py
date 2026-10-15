import random
class BankAccount(object):
    def __init__(self,name,account_type,balance=0):
        self.name = name
        self.account_type = account_type
        self.balance = balance

        #generate an ID for the new account 

        self.account_number=random.randint(100000,999999)

        self.filename=str(self.account_number)+"_"+self.account_type+"_"+self.name+".txt"

        #create an empty transaction file

        with open(self.filename, "w") as file:
            file.write("Transaction History:\n")

         #   Implement a function for depositing money into the account
    
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount

        with open(self.filename, 'a') as file:
            file.write(f"Deposited:  ${amount:.2f} | New Balance: ${self.balance:.2f}\n")


    #Implement a function for withdrawing money from the account

    def withdraw(self,amount):
        if amount > self.balance:
            print("Your account balance is less than $", amount)
        elif amount>0:
            self.balance-=amount

        with open(self.filename,'a') as file:
            file.write(f"Withdrew:  ${amount:.2f} | New Balance: ${self.balance:.2f}\n")
    

    #Implement a function for getting the account’s balance.
    def check_balance(self):
        return self.balance

    #Implement three separate functions for retrieving the user ID, username, and account type.

    def user_id(self):
        return self.account_number
    def username(self):
        return self.name
    def account_type(self):
        return self.account_type

    
    #Implement a function for getting transaction history by reading the statement file.
    def get_transaction_history(self):
        try:
            with open(self.filename,'r') as file:
                history= file.read()
                return history
        except FileNotFoundError:
            return "Error: Statement File could not be found"

if __name__ == "__main__":
    print("**********Running Bank Account Project Test**************")

    client1= BankAccount("Alice","Savings",1000)
    client2=BankAccount("Smith","Chequing",5000)
    client3=BankAccount("Raaz","chequing",9900)

    #Apply different transactions to Client 1 (Alice)
    print(f"Applying transactions for {client1.username()} (ID: {client1.user_id()})...")
    client1.deposit(250.50)
    client1.withdraw(100.00)
    client1.withdraw(1500.00)  # Should trigger an error printout
    
    print("\n--- Reading Alice's File ---")
    print(client1.get_transaction_history())
    print("-" * 40)

    # 3. Apply different transactions to Client 2 (Smith)
    print(f"Applying transactions for {client2.username()} (ID: {client2.user_id()})...")
    client2.deposit(50.00)
    client2.withdraw(25.00)
    
    print("\n--- Reading Bob's File ---")
    print(client2.get_transaction_history())
    print("-" * 40)

