#!/usr/bin/python3


def calculate(x_position, depth) -> int:
    """ Calculates final result """
    return x_position * depth
    
   
def main():

    try:
        file = open('day2.txt', "r")

        x_position = 0
        depth = 0

        for line in file:
            move_value = int(line[-2])
            command = line[:-3]

            if command == 'down': # if command down. Dive towards the bottom of the sea
                depth += move_value
            if command == 'up': # if command up. Dive towards the surface
                depth -= move_value
            if command == 'forward': # if command forward. Move forward
                x_position += move_value

        # Calculate final position.
        result = calculate(x_position, depth)
        print(f"Final answer is:{result}")
        
    except FileNotFoundError:
        print('File not found')
  

if __name__ == "__main__":
    main()