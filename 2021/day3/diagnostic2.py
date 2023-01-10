#!/usr/bin/python3

import numpy as np

def to_decimal(data:list) -> int:
    """
    Takes list of bits 
    Example: [1 0 1 1 0 1 0 1 1 0 1 0]

    Returns: Decimal number converted from binary.
    """

    binary = ''
    for i in data:
        binary += str(i)
        
    decimal = int(binary, 2)
    return decimal


def calculate(list_of_bits, o2=True) -> list[int]:
    """
        Calculates oxygen generator and co2 scrubber rates from list of binaries (diagnostig report)

        Parameters:
        -----------
            diagnostic report (list of bits)
            o2 = True
                calculates oxygen generator rate
            o2 = False
                calculates co2 scrubber rate.
        
        Returns:
        --------
            Oxygen generator rate or co2 scrubber rate as list of bits 
                list[int]

        Notes:
        ------
        Oxtgen generator rate:
            Determites the most common value (0 or 1) in the current bit position
            Keeps only numbers with that bit in that position
        Co2 scrubber rate:
            Determites the least common value (0 or 1) in the current bit position
            Keeps only numbers with that bit in that position
    """
    
    data = np.array(list_of_bits)
    i = 0
    while i < 12:
        size = len(data)
        zeros = (data[0:size,i] == 0).sum()
        ones = (data[0:size, i] == 1).sum()

        if ones >= zeros:
            # Get positions(index) of zeros or ones.
            zero_indexes = np.where(data[0:size,i] == 0)
            one_indexes = np.where(data[0:size,i] == 1)
            if size == 1:
                break
            if o2 == True:
                data = np.delete(data, zero_indexes, 0)
            else:
                data = np.delete(data, one_indexes, 0)
        else:
            zero_indexes = np.where(data[0:size,i] == 1)
            one_indexes = np.where(data[0:size,i] == 0)
            if size == 1:
                break
            if o2 == True:
                data = np.delete(data, zero_indexes, 0)
            else:
                data = np.delete(data, one_indexes, 0)
        i+=1
    return(data[0])

                
    

def main():

    try:
        file = open("day3.txt", "r")

        # list of lines in txt file
        lines = [line.rstrip("\n") for line in file]
        bits = []
        list_of_bits = []

        # Separate each bit from lines 
        j = 0
        while j < len(lines):
            for i in range(0, 12):
                bits.append(int(lines[j][i]))
            j += 1
        
        #  a list what contains sublists (12 bits/ one line per sublist)
        list_of_bits = [bits[x : x + 12] for x in range(0, len(bits), 12)]

        
        o2_data = calculate(list_of_bits)
        co2_data = calculate(list_of_bits, o2=False)
        
        o2_decimal = to_decimal(o2_data)
        co2_decimal = to_decimal(co2_data)
        
        # calculate final answer
        final = o2_decimal * co2_decimal

        print(f'Life support rating:{final}')
        file.close()
        
    except FileNotFoundError:
        print('File not found!')

        
if __name__ == "__main__":
    main()