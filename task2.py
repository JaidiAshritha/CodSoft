print("\n===================================")
print("      WELCOME TO CALCULATOR")
print("===================================\n")

num1 = float(input("Enter First Number  : "))
num2 = float(input("Enter Second Number : "))

print("\nChoose an Operation")
print("-----------------------------------")
print("1. Addition       (+)")
print("2. Subtraction    (-)")
print("3. Multiplication (*)")
print("4. Division       (/)")
print("5. Modulus        (%)")
print("6. Power          (^)")
print("-----------------------------------")

choice = input("Enter your choice (1-6): ")

print("\n===================================")

if choice == '1':
    result = num1 + num2
    print(f" Addition Result")
    print(f" {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f" Subtraction Result")
    print(f" {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f" Multiplication Result")
    print(f" {num1} × {num2} = {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f" Division Result")
        print(f" {num1} ÷ {num2} = {result}")
    else:
        print(" Error! Division by zero is not allowed.")

elif choice == '5':
    result = num1 % num2
    print(f" Modulus Result")
    print(f" {num1} % {num2} = {result}")

elif choice == '6':
    result = num1 ** num2
    print(f" Power Result")
    print(f" {num1}^{num2} = {result}")

else:
    print(" Invalid Choice! Please select from 1 to 6.")

print("===================================\n")
print(" Thank You for Using Calculator ")
print("===================================")