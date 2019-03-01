import os
import time

def main():

    a = time.clock()

    for i in range(80000):
        print(i)

    b = time.clock()
    print((b-a))

    list = [1]
    list.pop()
    print(len(list))
    return

if __name__ == '__main__':
    main()
