class Numbers:

    def __init__(self, Value):
        self.value = Value

    def CheckPrime(self):
        
        for i in range(self.value):
            if self.value <= 1:
                return False
            
            if self.value % 2 == 0:
                return False
        return True

    def CheckPerfect(self):
        
        sum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                sum += i
        return sum == self.value


    def Factors(self):
        self.factors = []
        # Loop through every number from 1 to n
        for i in range(1, self.value + 1):
            if self.value  % i == 0:
                self.factors.append(i)
        return self.factors

    def SumFactors(self):
        sum = 0
        for i in self.factors:
            sum += i
        return sum
        
        
def main():
    
    user_number = int(input("Enter the number: "))

    nobj = Numbers(user_number)
    
    nobj.CheckPrime()
    if nobj.CheckPrime() == True:
        print("This is prime number")
    else:
        print("This is NOT prime number")

    nobj.CheckPerfect()
    if nobj.CheckPerfect == True:
        print("This is perfect number")
    else:
        print("This is NOT perfect number")

    
    print(f"Factor number of {user_number} is: {nobj.Factors()}")

    print(f"Sum of all factors number is: {nobj.SumFactors()}")
    
if __name__ == "__main__":
    main()