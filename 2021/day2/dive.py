#!/usr/bin/python3


def calculate(x_position, y_position) -> int:
    return x_position * y_position
    
   

def main():

    x_position = 0
    depth = 0
    filepath = 'day2.txt'

    file = open(filepath, "r")

    for line in file:
        amount = int(line[-2])
        command = line[:-3]

        if command == 'down':
            depth += amount
        if command == 'up':
            depth -= amount
        if command == 'forward':
            x_position += amount

    
    result = calculate(x_position, depth)
    print(f"First answer is:{result}")
  

if __name__ == "__main__":
    main()