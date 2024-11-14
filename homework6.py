def main():
    print("choose one of the options below: ")
    print("1: save in list")
    print("2: save in dictionary")
    print("3: save in tuple")
    print("4: save in set")

    choice = input("your choice: ")
    if choice == "1":
        values = []
        for i in range(5):
            value = input(f"value {i+1}: ")
            values.append(value)
        print("list: ", values)
    elif choice == "2":
        values = []
        for i in range(5):
            key = input(f"key {i+1}: ")
            value = input(f"value {i+1}: ")
            values[key] = value
        print("dict: ", values)
    elif choice == "3":
        values = []
        for i in range(5):
            value = input(f"value {i+1}: ")
            values.append(value)
        values = tuple(values)
        print("tuple: ", values)
    elif choice == "4":
        values = set()
        for i in range(5):
            value = input(f"value {i+1}: ")
            values.add(value)
        print("set: ", values)
    else:
        print("invalid choice")
main()

