# This function checks if the student passed or failed. 
def check_result(mark):
    if mark >= 50:
        print("Pass")
    else:
        print("Fail")

# This Ask the user to enter their mark.
mark = int(input("Enter your mark: "))

# This calls the function.
check_result(mark)