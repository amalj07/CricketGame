import random


print("Welcome to Cricket Game")


Rules = "The game is between user and computer. Each one has one wicket. The accepted numbers are 0, 1, 2, 3, 4, 5, 6" \
        "While batting if 0 is entered then the runs entered by bowler will add to the batsman's runs. If user is " \
        "batting first, user should defend computer from taking more than your runs. If you are bowling first you " \
        "should score more runs than computer has scored"
while True:
    read_rules = input("Do you want to read the rules (Y/N): ")
    if read_rules == "Y" or read_rules == "y":
        print(Rules)
        break
    elif read_rules == "N" or read_rules == "n":
        break
    else:
        print("You entered invalid key")
        continue

print("Tossing the coin....")

toss_list = ["H", "T"]
toss_int = random.randint(0, 1)
toss = toss_list[toss_int]
while True:
    try:
        toss_called = input("Heads or Tails (H/T): ")
        if toss_called == "H" or toss_called == "h":
            toss_called = "H"
            break
        elif toss_called == "T" or toss_called == "t":
            toss_called = "T"
            break
        else:
            print("You entered invalid choice: ", toss_called)
            continue
    except ValueError:
        print("You entered invalid key")
        continue

if toss == toss_called:
    print("You won the toss")
    user_innings = input("Bat or Bowl: ")
    if user_innings == "Bat" or user_innings == "bat":
        print("Get ready for Batting")
    else:
        print("Get ready for Bowling")
else:
    print("You lost the toss")
    computer_innings_list = ["Batting", "Bowling"]
    computer_innings_list_int = random.randint(0, 1)
    computer_innings = computer_innings_list[computer_innings_list_int]
    if computer_innings == "Batting":
        print("Computer selected Batting")
        print("Get ready to Bowling")
        user_innings = "Bowling"
    else:
        print("Computer selected Bowling")
        print("Get ready to Bat")
        user_innings = "Bat"

user_runs = 0
cmp_runs = 0
user_bowl = 1
cmp_bowl = 1

if user_innings == "Bat" or user_innings == "bat":
    total_user_runs = 0
    while user_runs != cmp_bowl:
        cmp_bowl = random.randint(0, 6)
        while True:
            try:
                user_runs = int(input("Enter runs: "))
                if user_runs not in range(0, 7):
                    print("You entered: ", user_runs)
                    print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                    continue
                else:
                    break
            except ValueError:
                print("You entered invalid key")
                print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                continue
        if user_runs != cmp_bowl:
            if user_runs == 0:
                print("Computer bowl: ", cmp_bowl)
                total_user_runs = total_user_runs + cmp_bowl
                print("Your total runs: ", total_user_runs)
            else:
                print("Computer bowl: ", cmp_bowl)
                total_user_runs = total_user_runs + user_runs
                print("Your total runs: ", total_user_runs)
        else:
            print("Computer and you entered the same number: ", user_runs, "You're OUT")
            print("Your runs: ", total_user_runs)
            print("You need to defend computer from taking ", total_user_runs)
            break
    print("Get ready to bowl, Computer is batting")
    total_cmp_runs = 0
    while cmp_runs != user_bowl:
        if total_cmp_runs <= total_user_runs:
            cmp_runs = random.randint(0, 6)
            while True:
                try:
                    user_bowl = int(input("Enter runs: "))
                    if user_bowl not in range(0, 7):
                        print("You entered: ", user_bowl)
                        print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                        continue
                    else:
                        break
                except ValueError:
                    print("You entered invalid key")
                    print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                    continue
            if cmp_runs != user_bowl:
                if cmp_runs == 0:
                    print("Computer run: ", cmp_runs)
                    total_cmp_runs = total_cmp_runs + user_bowl
                    print("Computer total runs: ", total_cmp_runs)
                else:
                    print("Computer run: ", cmp_runs)
                    total_cmp_runs = total_cmp_runs + cmp_runs
                    print("Computer total runs: ", total_cmp_runs)
            else:
                print("Computer and you entered the same number: ", user_bowl, "Computer is OUT")
                if total_user_runs == total_cmp_runs:
                    print("Game draw")
                    print("Your runs: ", total_user_runs)
                    print("Computer runs: ", total_cmp_runs)
                else:
                    print("You Won")
                    print("Your runs: ", total_user_runs)
                    print("Computer runs: ", total_cmp_runs)
                    break
        else:
            print("Computer Won")
            print("Your runs: ", total_user_runs)
            print("Computer runs: ", total_cmp_runs)
            break

else:
    total_cmp_runs = 0
    while cmp_runs != user_bowl:
        cmp_runs = random.randint(0, 6)
        while True:
            try:
                user_bowl = int(input("Enter runs: "))
                if user_bowl not in range(0, 7):
                    print("You entered: ", user_bowl)
                    print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                    continue
                else:
                    break
            except ValueError:
                print("You entered invalid key")
                print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                continue
        if cmp_runs != user_bowl:
            if cmp_runs == 0:
                print("Computer run: ", cmp_runs)
                total_cmp_runs = total_cmp_runs + user_bowl
                print("Computer total runs: ", total_cmp_runs)

            else:
                print("Computer run: ", cmp_runs)
                total_cmp_runs = total_cmp_runs + cmp_runs
                print("Computer total runs: ", total_cmp_runs)
        else:
            print("Computer and you entered the same number: ", user_bowl, "Computer is OUT")
            print("Computer runs: ", total_cmp_runs)
            print("You need to take ", total_cmp_runs + 1, "to win")
            break
    print("Get ready to bat, Computer is bowling")
    total_user_runs = 0
    while user_runs != cmp_bowl:
        if total_user_runs <= total_cmp_runs:
            cmp_bowl = random.randint(0, 6)
            while True:
                try:
                    user_runs = int(input("Enter runs: "))
                    if user_bowl not in range(0, 7):
                        print("You entered: ", user_runs)
                        print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                        continue
                    else:
                        break
                except ValueError:
                    print("You entered invalid key")
                    print("accepted numbers: 0, 1, 2, 3, 4, 5, 6")
                    continue
            if user_runs != cmp_bowl:
                if user_runs == 0:
                    print("Computer bowl: ", cmp_bowl)
                    total_user_runs = total_user_runs + cmp_bowl
                    print("Your total runs: ", total_user_runs)
                else:
                    print("Computer bowl: ", cmp_bowl)
                    total_user_runs = total_user_runs + user_runs
                    print("Your total runs: ", total_user_runs)
            else:
                print("Computer and you entered the same number: ", user_runs, "You're OUT")
                if total_cmp_runs == total_user_runs:
                    print("Game draw")
                    print("Your runs: ", total_user_runs)
                    print("Computer runs: ", total_cmp_runs)
                else:
                    print("Your runs: ", total_user_runs)
                    print("Computer runs: ", total_cmp_runs)
                    print("Computer Won")
                    break
        else:
            print("You Won")
            print("Your runs: ", total_user_runs)
            print("Computer runs: ", total_cmp_runs)
            break