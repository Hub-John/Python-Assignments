class Circle:
    # Class Variable
    PI = 3.14 

    # Class Constructor
    def __init__(self):
        # Intance Variable
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    # Four Instance Method 
    def Accept(self):
        user_input = input("Enter the radius of the circle: ")
        self.radius = float(user_input)
        
    def CalculateArea(self):
        self.area = Circle.PI * (self.radius ** 2)
    
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area:.2f}")
        print(f"Circumference: {self.circumference:.2f}")


def main():
    
    c1 = Circle()
    c1.Accept()
    c1.CalculateArea()
    c1.CalculateCircumference()
    c1.Display()

    c2 = Circle()
    c2.Accept()
    c2.CalculateArea()
    c2.CalculateCircumference()
    c2.Display()
    

if __name__ == "__main__":
    main()