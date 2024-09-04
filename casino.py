import random

MAX_LINES = 3
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "$": 4,
    "#": 6,
    "*": 10,
    "&": 12
}

symbol_value = {
    "$": 10,
    "#": 8,
    "*": 5,
    "&": 3
}

def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end="  ")
            else:
                print(column[row], end="  ")

        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  
            winnings += values[symbol] * bet
    
    return winnings

def deposit():
    while True:
        amount = input("Enter a deposit amount $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter a number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Line must be between (1-{MAX_LINES}).")
        else:
            print("Please enter a valid number of lines.")

def get_bet(max_bet, lines):
    while True:
        bet = input(f"Enter an amount to bet on each line (${MIN_BET}-${max_bet // lines}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= max_bet // lines:
                return bet
            else:
                print(f"Bet must be between (${MIN_BET}-${max_bet // lines}).")
        else:
            print("Please enter a valid amount.")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet(balance, lines)
        total_bet = bet * lines
        if total_bet > balance:
            print("Insufficient amount: Please enter a valid amount.")
        else:
            print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
    
            break

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    balance += winnings - total_bet
    print(f"You have ${balance} left.")

    if balance > MIN_BET:
        again = input("Would you like to play again? (y/n): ")
        if again.lower() == "y":
            spin(balance)
        else:
            print("Thanks for playing. Goodbye!")
    else:
        print("Insufficient Balance to spin again, Please deposit before spinning. Bye!")
        quit()

def main():
    balance = deposit()
    spin(balance)

main()
