#!/usr/bin/python3


def calculate_power_consumption(rates: tuple) -> int:
    """
    Converts "gamma" and "epsilon" binary rates to decimal numbers

    Returns:
        "Amount of "power consuption"
    """
    gamma, epsilon = rates
    print(gamma)
    gamma_rate_decimal = int(gamma, 2)
    epsilon_rate_decimal = int(epsilon, 2)
    answer = gamma_rate_decimal * epsilon_rate_decimal
    return answer


def calculate_gamma_epsilon_rate(list_of_bits: list) -> tuple:
    """
    Calculates gamma and epsilon rates. Counts most common bits

    Return:
        Counted gamma rate and epsilon rate values as a binary numbers
    """
    gamma_rate = ""
    epsilon_rate = ""
    for bits in list_of_bits:
        if bits.count("1") > bits.count("0"):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return gamma_rate, epsilon_rate


def main():
    
    
    try:
        file = open("test.txt", "r")

        bits = []
        list_of_bits = []
        lines = [line.rstrip("\n") for line in file]

        j = 0
        while j < 12:
            for i in range(0, len(lines)):
                bits.append(lines[i][j])
            j += 1
        
        # list what contains sublists (first sublist contains all firts numbers from lines. second contains all 2:nd...etc)
        list_of_bits = [bits[x : x + len(lines)] for x in range(0, len(bits), len(lines))]
        print(list_of_bits)
        rates = calculate_gamma_epsilon_rate(list_of_bits)
    
        final = calculate_power_consumption(rates)
        print(f"Power consumption as a decimal number {final}")
        
        file.close()
    except FileExistsError:
        print('file not found')


if __name__ == "__main__":
    main()
