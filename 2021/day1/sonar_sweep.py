#!/usr/bin/python3

def count_measurements(lines: list) -> int:
    """iterate list of numbers while list lenght is bigger than 2

    Return:
        increase: Count of numbers what is increased compared to the previous number of the list.

        decrease: Count of numbers what is decreased compared to the previous number of the list
    """

    decrease = 0
    increase = 0

    while len(lines) >= 2:
        last = lines[-1]
        secondlast = lines[-2]

        if last > secondlast:
            increase += 1
        else:
            decrease += 1
        lines.pop()

    return increase, decrease


def make_list_of_three_measurements(lines: list) -> list:
    """
    Iterate through the list and counts three last numbers together and removes last one.

    Return:
        New list of measurements
    """
    measurements = []

    while len(lines) >= 3:
        last_three = sum(lines[-3:])
        measurements.insert(0, last_three)
        lines.pop()

    return measurements


def main():
    try:
        file = open('day1.txt', "r")
        lines = [int(line.rstrip("\n")) for line in file]
        
        measurements = make_list_of_three_measurements(lines)

        increase, decrease = count_measurements(measurements)

        print(f"Increase: {increase}, Decrease: {decrease} ")
    except FileExistsError:
        print('File not found!')


if __name__ == "__main__":
    main()
