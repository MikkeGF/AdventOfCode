#!/usr/bin/python3

def calculate(aim: int, amount:int) -> int:
    return aim * amount

def main():
    x_position = 0
    aim = 0
    depth = 0
    filepath = 'day2.txt'

    file = open(filepath, "r")

    for line in file:
        amount = int(line[-2])
        command = line[:-3]

        if command == 'down':
            aim += amount
        if command == 'up':
            aim -= amount
        if command == 'forward':
            x_position += amount
            depth += calculate(aim, amount)
        
    final = calculate(x_position, depth)
    print(f"final asnwer: {final}")
    file.close()

if __name__ == "__main__":
    main()
