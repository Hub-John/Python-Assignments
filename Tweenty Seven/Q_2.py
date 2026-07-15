class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
        
    def Deposit(self):
        self.Amount = int(input("Enter the Amount: "))
        
    def Withdraw(self):
        self.Amount = self.Amount - int(input("Enter the Withdraw Amount: "))

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Estimated Interest: {Interest}")

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")
        print("-------------------------------")

def main():
    
    bobj1 = BankAccount('Vishal', '')
    bobj1.Deposit()
    bobj1.Withdraw()
    bobj1.CalculateInterest()
    bobj1.Display()
    
    bobj2 = BankAccount('Johnson', '')
    bobj2.Deposit()
    bobj2.Withdraw()
    bobj2.CalculateInterest()
    bobj2.Display()
    
if __name__ == "__main__":
    main()