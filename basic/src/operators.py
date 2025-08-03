# basic/src/operators.py

def operators():
    while True:
        print("\n=== Operator Categories ===")
        print("1. Arithmetic")
        print("2. Comparison")
        print("3. Logical")
        print("4. Assignment")
        print("0. Exit")

        choice = input("Choose an option (0-4): ").strip()

        if choice == "1":
            arithmetic_operators()
        elif choice == "2":
            comparison_operators()
        elif choice == "3":
            logical_operators()
        elif choice == "4":
            assignment_operators()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 0 to 4.")


def get_two_numbers():
    while True:
        try:
            values = input("Enter two numbers separated by space: ").split()
            if len(values) != 2:
                raise ValueError("Please enter exactly two values.")
            x, y = map(float, values)
            return x, y
        except ValueError as e:
            print(f"❌ Error: {e}")


def get_two_strings():
    values = input("Enter two values separated by space: ").split()
    if len(values) != 2:
        print("❌ You must enter exactly two values.")
        return get_two_strings()
    return values[0], values[1]


def arithmetic_operators():
    print("\n=== Arithmetic Operators ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")

    choice = input("Choose an operator (1-5): ").strip()
    x, y = get_two_numbers()

    try:
        if choice == "1":
            print(f"✅ Result: {x} + {y} = {x + y}")
        elif choice == "2":
            print(f"✅ Result: {x} - {y} = {x - y}")
        elif choice == "3":
            print(f"✅ Result: {x} * {y} = {x * y}")
        elif choice == "4":
            print(f"✅ Result: {x} / {y} = {x / y}")
        elif choice == "5":
            print(f"✅ Result: {x} % {y} = {x % y}")
        else:
            print("❌ Invalid arithmetic choice.")
    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")


def comparison_operators():
    print("\n=== Comparison Operators ===")
    print("1. Equal to (==)")
    print("2. Not equal to (!=)")
    print("3. Greater than (>)")
    print("4. Less than (<)")
    print("5. Greater than or equal (>=)")
    print("6. Less than or equal (<=)")

    choice = input("Choose a comparison operator (1-6): ").strip()
    x, y = get_two_strings()

    if choice == "1":
        print(f"✅ Result: {x} == {y} ➜ {x == y}")
    elif choice == "2":
        print("Result: {} != {} -> {}".format(x, y, x != y))
    elif choice == "3":
        print(f"✅ Result: {x} > {y} ➜ {x > y}")
    elif choice == "4":
        print(f"✅ Result: {x} < {y} ➜ {x < y}")
    elif choice == "5":
        print(f"✅ Result: {x} >= {y} ➜ {x >= y}")
    elif choice == "6":
        print(f"✅ Result: {x} <= {y} ➜ {x <= y}")
    else:
        print("❌ Invalid comparison choice.")


def logical_operators():
    print("\n=== Logical Operators ===")
    print("1. and")
    print("2. or")
    print("3. not (first value only)")

    choice = input("Choose a logical operator (1-3): ").strip()
    values = input("Enter two values (True/False) separated by space: ").split()

    if len(values) != 2 or not all(v in ["True", "False"] for v in values):
        print("❌ Error: Please enter only 'True' or 'False'.")
        return logical_operators()

    x = values[0] == "True"
    y = values[1] == "True"

    if choice == "1":
        print(f"✅ Result: {x} and {y} ➜ {x and y}")
    elif choice == "2":
        print(f"✅ Result: {x} or {y} ➜ {x or y}")
    elif choice == "3":
        print(f"✅ Result: not {x} ➜ {not x}")
    else:
        print("❌ Invalid logical choice.")


def assignment_operators():
    print("\n=== Assignment Operators ===")
    print("1. = (Assignment)")
    print("2. += (Addition Assignment)")
    print("3. -= (Subtraction Assignment)")
    print("4. *= (Multiplication Assignment)")
    print("5. /= (Division Assignment)")
    print("6. %= (Modulo Assignment)")

    choice = input("Choose an assignment operator (1-6): ").strip()
    x, y = get_two_numbers()

    try:
        if choice == "1":
            x = y
            print(f"✅ x = y ➜ x = {x}")
        elif choice == "2":
            x += y
            print(f"✅ x += y ➜ x = {x}")
        elif choice == "3":
            x -= y
            print(f"✅ x -= y ➜ x = {x}")
        elif choice == "4":
            x *= y
            print(f"✅ x *= y ➜ x = {x}")
        elif choice == "5":
            x /= y
            print(f"✅ x /= y ➜ x = {x}")
        elif choice == "6":
            x %= y
            print(f"✅ x %= y ➜ x = {x}")
        else:
            print("❌ Invalid assignment operator choice.")
    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")


