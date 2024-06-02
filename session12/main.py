import module as calc

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Choose an operation (1/2/3/4): "))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        print(f"{num1} + {num2} = {calc.add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {calc.subtract(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
    elif choice == 4:
        print(f"{num1} / {num2} = {calc.divide(num1, num2)}")
    else:
        print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()