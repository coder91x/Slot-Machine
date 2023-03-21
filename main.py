import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3

symbol_counts = {
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


def get_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def generate_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbol_counts.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    return columns


def print_spin_matrix(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end='|')
            else:
                print(col[row])


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


def game(balance):
    lines = get_number_0f_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        print(f"You are betting {bet}$ on {lines} lines. Your total bet is ${total_bet}.")
        if total_bet >= balance:
            print(f"You have exceeded your balance. Your current balance is {balance}")
        else:
            break
    slots = generate_spin(ROWS, COLS, symbol_counts)
    print_spin_matrix(slots)
    winnings, winnings_lines = get_winnings(slots, lines, bet, symbol_values)
    print(f"You have won ${winnings} on line", *winnings_lines)
    return winnings - total_bet


def main():
    balance = get_deposit()
    while True:
        print(f"Current balance is {balance}")
        spin = input("Press enter to continue or q to quit")
        if spin == 'q':
            break
        else:
            balance += game(balance)
    print(f"You have left with ${balance}")



main()
