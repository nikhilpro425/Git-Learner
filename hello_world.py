# Following Code is or a Basic 2 number Calculator :

print("\t\t\t\t Basic Two Number Calculator")
print("\t Choice 1 : Return Sum of 2 numbers")
print("\t Choice 2 : Return Difference of 2 numbers")
print("\t Choice 3 : Return Product of 2 numbers")
print("\t Choice 4 : Return Quotient of 2 numbers")
print("\t Choice 5 : Return Exponent of 2 numbers")
choice1 = int(input(" Enter any Choice[1-5] \n\t\t\t\tOR \nEnter any other number to EXIT : "))
num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))


def calculator(choice, a, b):
    if choice == 1:
        return "Sum is " + str(a + b)
    elif choice == 2:
        return "Difference is " + str(abs(a-b))
    elif choice == 3:
        return "Product is " + str(a*b)
    elif choice == 4:
        return "Quotient is " + str(a/b)
    elif choice == 5:
        return str(a) + " to the power " + str(b) + " is " + str(a**b)
    else:
        return "Thank You"


result = (calculator(choice1, num1, num2))
print(result)
