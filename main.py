MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_values = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def get_deposit():
    while True:
        amount = input("Please enter the amount to be deposited: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than zero")
        else:
            print("Please enter a valid number as deposit")
    return amount


def get_number_0f_lines():
    while True:
        lines = input("Please enter the number of lines you want to play: ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter the lines between {MIN_LINES} and {MAX_LINES}")
        else:
            print("Please enter a valid number for number of lines")
    return lines


def get_bet():
    while True:
        bet = input("Please enter the bet you want to place: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter the bet between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a valid number for bet")
    return bet


def main():
    amount = get_deposit()
    lines = get_number_0f_lines()
    bet = get_bet()


main()
