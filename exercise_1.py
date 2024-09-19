# Write a Python program that asks the user to input 3 numbers,
# and then the program will find and print the maximum value among the entered numbers.
# (Note: You cannot use built-in functions like max() or any lists)
number_1 = input("choose random number #1: ")
number_2 = input("choose random number #2: ")
number_3 = input("choose random number #3: ")

# Check user input is number
if number_1.isnumeric() and number_2.isnumeric() and number_3.isnumeric():

    # str to number
    number_1 = float(number_1)
    number_2 = float(number_2)
    number_3 = float(number_3)

    max_number = number_1

    if max_number < number_2:
        max_number = number_2

    if max_number < number_3:
        max_number = number_3

    print(max_number)

else:
    print("Only positive numbers are accepted.")

