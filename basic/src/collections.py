# basic/src/collections.py

def collections():
    print("=== Python Collections Menu ===")

    while True:
        print("\nChoose a collection type:")
        print("1. List")
        print("2. Tuple")
        print("3. Set")
        print("4. Dictionary")
        print("0. Exit")

        choice = input("Enter your choice (0–4): ").strip()

        if choice == "1":
            handle_list()
        elif choice == "2":
            handle_tuple()
        elif choice == "3":
            handle_set()
        elif choice == "4":
            handle_dict()
        elif choice == "0":
            print("Exiting collections program.")
            break
        else:
            print("❌ Invalid input. Please enter a number from 0 to 4.")


def handle_list():
    alist = [1, 2, 3, 4, 5]
    print(f"\n📦 Here is a list: {alist}")
    print("Choose a list operation:")
    print("1. Length")
    print("2. Indexing (first element)")
    print("3. Slicing (index 1 to 2)")
    print("4. Iteration")
    print("5. Append an element")

    choice = input("Enter your choice (1–5): ").strip()
    if choice == "1":
        print(f"✅ Length: {len(alist)}")
    elif choice == "2":
        print(f"✅ First element: {alist[0]}")
    elif choice == "3":
        print(f"✅ Sliced [1:3]: {alist[1:3]}")
    elif choice == "4":
        print("✅ Iteration:")
        for element in alist:
            print(f" - {element}")
    elif choice == "5":
        alist.append(6)
        print(f"✅ After appending 6: {alist}")
    else:
        print("❌ Invalid choice.")


def handle_tuple():
    atuple = (1, 2, 3, 4, 5)
    print(f"\n📦 Here is a tuple: {atuple}")
    print("Choose a tuple operation:")
    print("1. Length")
    print("2. Indexing (first element)")
    print("3. Slicing (index 1 to 2)")
    print("4. Iteration")

    choice = input("Enter your choice (1–4): ").strip()
    if choice == "1":
        print(f"✅ Length: {len(atuple)}")
    elif choice == "2":
        print(f"✅ First element: {atuple[0]}")
    elif choice == "3":
        print(f"✅ Sliced [1:3]: {atuple[1:3]}")
    elif choice == "4":
        print("✅ Iteration:")
        for element in atuple:
            print(f" - {element}")
    else:
        print("❌ Invalid choice.")
        print("ℹ️ Note: Tuples are immutable — you can't modify them.")


def handle_set():
    aset = {1, 2, 3, 4, 5}
    print(f"\n📦 Here is a set: {aset}")
    print("Choose a set operation:")
    print("1. Length")
    print("2. Iteration")
    print("3. Add an element")

    choice = input("Enter your choice (1–3): ").strip()
    if choice == "1":
        print(f"✅ Length: {len(aset)}")
    elif choice == "2":
        print("✅ Iteration:")
        for element in aset:
            print(f" - {element}")
    elif choice == "3":
        aset.add(6)
        print(f"✅ After adding 6: {aset}")
    else:
        print("❌ Invalid choice.")


def handle_dict():
    adict = {"key1": "value1", "key2": "value2", "key3": "value3"}
    print(f"\n📦 Here is a dictionary: {adict}")
    print("Choose a dictionary operation:")
    print("1. Length")
    print("2. Iteration (key-value pairs)")
    print("3. Add/update a key-value pair")

    choice = input("Enter your choice (1–3): ").strip()
    if choice == "1":
        print(f"✅ Length: {len(adict)}")
    elif choice == "2":
        print("✅ Key-value pairs:")
        for key, value in adict.items():
            print(f" - {key}: {value}")
    elif choice == "3":
        adict.update({"key4": "value4"})
        print(f"✅ After update: {adict}")
    else:
        print("❌ Invalid choice.")

