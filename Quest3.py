# This function calculates the student's grade.
def calculate_grade(mark):
    if mark >= 80:
        print("A")
    elif mark >= 70:
        print("B")
    elif mark >= 60:
        print("C")
    elif mark >= 50:
        print("D")
    else:
        print("F")


# Ask the user to enter their mark.
mark = int(input("Enter your mark: "))

# Call the function.
calculate_grade(mark)