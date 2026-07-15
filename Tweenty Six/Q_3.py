class Arithmetic:

    # Class Constructor 
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Instance Method
    def Accept(self):

        try:
            self.v1 = int(input("Enter the first number: "))
            self.v2 = int(input("Enter the second number: "))
       
        except ValueError as vobj:
            print("Exception occured due to invalid data type:", vobj)

        except ZeroDivisionError as zobj:
            print("Exception occured due to second operand is zero:", zobj)

        except Exception as eobj:
            print("Exception occured:", eobj)
        

    def Addition(self):
        print("Additon is: ", self.v1 + self.v2)

    def Substraction(self):
        print("Substraction is: ", self.v1 - self.v2)

    def Multiplication(self):
        print("Multiplication is: ", self.v1 * self.v2)

    def Division(self):
        print("Division is: ", self.v1 / self.v2)


def main():
    aobj = Arithmetic()

    aobj.Accept()
    aobj.Addition()
    aobj.Substraction()
    aobj.Multiplication()
    aobj.Division()

    
if __name__ == "__main__":
    main()