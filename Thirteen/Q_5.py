
# Write a program which accepts marks and displays grade.

def DisplyGrade(grade):

    if(grade >= 75):
        print("Distinction")
    elif(grade >= 60):
        print("First Class")
    elif(grade >= 50):
        print("Second Class")
    else:
        print("Fail")
    

def main():

    Marks = int(input("Enter your percentage(%): "))

    DisplyGrade(Marks)

if __name__ == "__main__":
    main()