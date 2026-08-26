# This function checks the person's age category.
def age_category(age):
    if age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior")

# The ask the user to enter their age.
age = int(input("Enter your age: "))

# This calls the function.
age_category(age)