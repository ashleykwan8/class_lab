"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:

    input_string = input("enter your equation: ")
    # print(input_string)

    tokens = input_string.split()
# print(tokens)
    if (tokens[0] == 'q'):
        break

    else:
        if (tokens[0] == '+'):
            result = add(float(tokens[1]),float(tokens[2]))
            print(result)
        elif(tokens[0] == '-'):
            result = subtract(float(tokens[1]),float(tokens[2]))
            print(result)
        elif(tokens[0] == '*'):
            result = multiply(float(tokens[1]),float(tokens[2]))
            print(result)
        elif(tokens[0] == '/'):
            result = divide(float(tokens[1]),float(tokens[2]))
            print(result)
        elif(tokens[0] == 'square'):
            result = square(float(tokens[1]))
            print(result)
        elif(tokens[0] == 'cube'):
            result = cube(float(tokens[1]))
            print(result)
        elif(tokens[0] == 'pow'):
            result = power(float(tokens[1]),float(tokens[2]))
            print(result)
        elif(tokens[0] == 'mod'):
            result = mod(float(tokens[1]),float(tokens[2]))
            print(result)

        