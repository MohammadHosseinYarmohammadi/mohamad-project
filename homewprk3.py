from colorama import Fore, Style


def main():
    num1 = int(input("Enter first number(between 6 and 10): "))
    num2 = int(input("Enter second number(between 6 and 10): "))
    results = []
    if 6 <= num1 <= 10 and 6 <= num2 <= 10:
        print(f'multiplication table {num1} and {num2} without rows and columns 2')
        for i in range(1, 9+1):
            row = []
            for j in range(1, 9+1):
                if i == 2 or j == 2:
                    continue
                result = i * j
                row.append(result)
                if i == 4 or j == 4:
                    print(f"{Fore.RED}{i * j:4}{Style.RESET_ALL}", end=' ')
                else:
                    print(f"{Fore.YELLOW}{i * j:4}{Style.RESET_ALL}", end=' ')
            results.append(row)
            print()
        print(f" list mul table:\n {results}")
        even_numbers = extract_even_numbers(results)
        print("")
        print(f" list extract_even_numbers: \n {even_numbers}")


    else:
        print('Enter numbers between 6 and 10')


def extract_even_numbers(table):
    even_numbers = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            number = table[i][j]
            if number % 2 == 0:
                even_numbers.append(number)
    return even_numbers
main()