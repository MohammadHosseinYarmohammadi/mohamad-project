from  colorama import Fore, Style
from random import randint

def register_user():
    users = {}
    for i in range(2):
        print(f"user registration number {i+1}")
        username = input("please enter your Username: ")
        password = input("please enter your Password(just enter the number): ")

        if password.isdigit():
            users[username] = {"password": password, "wins":0, "losses":0}
            print("registration successful")
        else:
            print("error!!!: password can only be a number")
            exit()
    print("users registration successfully done")
    return users

def guess_number_game(users):
    usernames = list(users.keys())
    for round_num in range(1, 6):
        print(f"\n {Fore.CYAN} round {round_num}{Style.RESET_ALL}")
        target_number = randint(1, 10)


        for i in range(len(usernames)):
            username = usernames[i]
            guess = int(input(f"{username} please guess the number between 1 to 10: "))

            if guess == target_number:
                print(f"{Fore.GREEN} congratulations! {username} your guess is correct {Style.RESET_ALL}")
                users[username]["wins"] += 1
                break
            else:
                print(f"{Fore.RED} unfortunately your guess is wrong {username} {Style.RESET_ALL}")
                users[username]["losses"] += 1

def display_results(users):
    print("\n the final results of the game: ")
    usernames = list(users.keys())

    for i in range(len(usernames)):
        username = usernames[i]
        variable = users[username]
        print(f"{username} wins: {variable["wins"]}, losses: {variable['losses']}")

        user1, user2 = usernames[0], usernames[1]
        if users[user1]["wins"] > users[user2]["wins"]:
            print(f"{Fore.GREEN} user {user1} is the final winner{Style.RESET_ALL}")
        elif users[user1]["wins"] < users[user2]["wins"]:
            print(f"{Fore.GREEN} user {user2} is the final winner{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW} the game is equal {Style.RESET_ALL}")

users = register_user()
guess_number_game(users)
display_results(users)
