#!/usr/bin/python3
import numpy as np


def read_bingo_numbers(path):
    """
        Reads first line of day4.txt and append numbers to list

        Returns
        
    """
    bingo_numbers=[]
    with open(path,'r') as file:
        content=file.readline().strip()
        for i in content.split('\n'):
            bingo_numbers.append(i.split(','))
        return bingo_numbers


def read_bingo_boards(path):

    import csv
    bingo_boards = []
   
    with open('text.txt') as f:
        
        for _ in range(2):
            next(f)
        reader = csv.reader(f, delimiter=' ')
        for i in reader:
            sub_list = list(filter(None, i))
            if sub_list != []:
                bingo_boards.append(sub_list)
    x = np.array(bingo_boards)
    bingo_boards = x.astype(np.int)
    return bingo_boards



def main():
    try:
        test = read_bingo_numbers('test.txt')
        
        boards = read_bingo_boards('test.txt')

    except FileNotFoundError:
        print('File not found!')
    
if __name__ == "__main__":
    main()    