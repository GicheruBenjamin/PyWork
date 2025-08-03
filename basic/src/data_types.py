# basic/src/data_types.py

import ast

def data_types():
    print("\n=== Data Types ===")
    print("\n=== Python Data Type Identifier ===")

    while True:
        print("\n--- Menu ---")
        print("1. Identify data type")
        print("0. Exit")

        choice = input("Choose an option (0 or 1): ").strip()

        if choice == "1":
            detect_data_type()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 0 or 1.")


def detect_data_type():
    print("\nType something, and I'll tell you its data type!")
    print("Examples: 42, 3.14, 'hello', [1,2], {\"a\":1}, None")

    raw_input = input("Enter a variable: ")

    try:
        # Safely parse the input as a Python literal (e.g., list, number, etc.)
        value = ast.literal_eval(raw_input)
    except (ValueError, SyntaxError):
        # If parsing fails, treat input as a plain string
        value = raw_input

    data_type = type(value).__name__

    print(f"✅ You entered a value of type: `{data_type}`")
    print(f"📦 Value: {value}")

