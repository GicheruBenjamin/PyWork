# basic/main.py

from basic.src import data_types, collections, operators

def main():
    print("\n=== Basic Menu ===")
    print("What do you want to know today?")
    print("1. Data types")
    print("2. Collections")
    print("3. Operators")
    print("0. Exit")

    choice = input("Enter your choice (0–3): ").strip()

    if choice == "1":
        data_types()
    elif choice == "2":
        collections()
    elif choice == "3":
        operators()
    elif choice == "0":
        print("Exiting basic program.")
    else:
        print("❌ Invalid input. Please enter a number from 0 to 3.")
        main()
    

if __name__ == "__main__":
    main()