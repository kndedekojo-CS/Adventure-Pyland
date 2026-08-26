# This function checks whether a number is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# This asks the user to enter an integer.
number = int(input("Enter an integer: "))
# This will call the function.
check_even_odd(number)