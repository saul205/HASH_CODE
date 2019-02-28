import os
import numpy as np

input = 'a_example.txt'
output = 'a_example.out'

with open(input) as f_in:
    # read first line
    numfotos = [int(x) for x in next(f_in).split()]
    matrix = []
    for line in f_in: # read rest of lines
        matrix.append([x for x in line.split()])


def resulttofile(res):
    with open(output, 'w') as f_out:
        for item in res:
            for subitem in item:
                f_out.write("%s " % subitem)
            f_out.write("\n")


def main():
    #Codigo aqui
    resulttofile(matrix)


if __name__ == '__main__':
    main()
