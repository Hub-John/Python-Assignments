
# Write a program which accepts radius of circle and prints area of circle.

def main():
    
    radius = int(input("Radius of Circle: "))

    pi_value = 3.14159

    AreaOfCircle = pi_value * (radius ** 2)

    print("Area of Rectangle is:", AreaOfCircle)

if __name__ == "__main__":
    main()