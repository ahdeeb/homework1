#Write a Python program that:
#1. Takes a positive integer 𝑛 from the user.
#2. Multiplies all the odd numbers between 1 and 𝑛 (inclusive).
#If the product exceeds 100, print "Multiplication exceeded" and stop the multiplication process.
#If there are no odd numbers, the program should simply return 1.
#If the multiplication process completes without exceeding 100, print the final product

number = input("choose a random positive number: ")

if number.isdigit() and int(number) > 0:

    i = 1
    multi_sum = 1
    while i <= int(number):
        if i % 2 == 1: #odd
            # sum = sum * i
            multi_sum *= i
        i += 1 

    if multi_sum > 100:
        print("Multiplication exceeded")
    else:
        print(multi_sum)
else:
   print("only positive numbers are accepted")
