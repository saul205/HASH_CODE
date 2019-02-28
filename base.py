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
    V = []
    H = []
    integercounter = 0
    for element in matrix:
        tmp = []
        tmptags = []
        tmp.append(str(integercounter))
        for i in range(int(element[1])):
            tmptags.append(element[2+i])
        tmp.append(tmptags)
        if element[0] is 'V':
            V.append(tmp)
        elif element[0] is 'H':
            H.append(tmp)
        integercounter = integercounter + 1




def testoutput():
    with open(output, 'w') as f_out:
        for item in V:
            for subitem in item:
                f_out.write("%s " % subitem)
            f_out.write("\n")
        for item in H:
            for subitem in item:
                f_out.write("%s " % subitem)
            f_out.write("\n")


def main():
    #Codigo aqui
    testoutput()


if __name__ == '__main__':
    main()
