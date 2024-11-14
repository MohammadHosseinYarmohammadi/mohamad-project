from random import randint, random

def main():
    random_number = randint(1, 10)
    print("a number between 1 and 100 has been selected try to find the number")
    for i in range(1, 10+1):
        guess = int(input(f" \n guess {i}:"))
        if guess < random_number:
            print("the selected number is larger")
        elif guess > random_number:
            print("the selected number is smaller")
        else:
            print(f"***congratulations*** \n your random_number is {random_number} and your guess is {guess}")
            break
    else:
        print("your guess is over")
main()

